#!/usr/bin/env python3
"""
Script to run TutorialMaker tests in multiple languages on CI/GitHub Actions
Optimized for execution in containers and headless environments
"""

import sys
import os
import json
import time
import tempfile
import subprocess
from pathlib import Path

# Default settings
DEFAULT_LANGUAGES = ["pt-BR", "es-419", "fr-FR"]
SLICER_TIMEOUT = 300  # 5 minutes timeout per test

class TutorialTestRunner:
    """Runner for tutorial tests in multiple languages"""
    
    def __init__(self, slicer_executable, tutorial_name=None, output_dir=None):
        self.slicer_executable = Path(slicer_executable)
        self.tutorial_name = tutorial_name or "TestTutorial"
        self.output_dir = Path(output_dir) if output_dir else Path.cwd() / "test_outputs"
        self.results = {}
        
        # Create output directory
        self.output_dir.mkdir(exist_ok=True)
        
    def run_test_for_language(self, language_code):
        """
        Runs test for a specific language using restart strategy:
        1. First session: Configure language and wait
        2. Second session: Execute tutorial with applied language
        
        Args:
            language_code (str): Language code
            
        Returns:
            dict: Test result
        """
        print(f"\\n=== Testing language: {language_code} ===")
        
        try:
            # Step 1: Configure language
            print("Step 1: Configuring language...")
            config_success = self._configure_language(language_code)
            
            if not config_success:
                return {
                    "language": language_code,
                    "tutorial": self.tutorial_name,
                    "status": "error",
                    "error": "Language configuration failed",
                    "execution_time": 0
                }
            
            # Step 2: Execute tutorial with configured language
            print("Step 2: Executing tutorial with applied language...")
            return self._run_tutorial_test(language_code)
            
        except Exception as e:
            print(f"💥 General error in test for {language_code}: {e}")
            return {
                "language": language_code,
                "tutorial": self.tutorial_name,
                "status": "exception",
                "error": str(e),
                "execution_time": 0
            }
    
    def _configure_language(self, language_code):
        """
        First session: Only configures the language in preferences
        
        Args:
            language_code (str): Language code
            
        Returns:
            bool: True if configuration was successful
        """
        config_script = self._create_language_config_script(language_code)
        
        try:
            # Simple command for configuration
            cmd = [str(self.slicer_executable), '--no-splash', '--python-script', config_script]
            
            print(f"Configuring: {' '.join(cmd[:2])} ...")
            
            start_time = time.time()
            
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                universal_newlines=True
            )
            
            # Short timeout for configuration (30 seconds)
            config_timeout = 30
            output_lines = []
            
            while True:
                if process.poll() is not None:
                    break
                    
                elapsed = time.time() - start_time
                if elapsed > config_timeout:
                    print(f"⏰ Configuration timeout after {elapsed:.1f}s")
                    process.terminate()
                    time.sleep(2)
                    if process.poll() is None:
                        process.kill()
                    return False
                
                try:
                    line = process.stdout.readline()
                    if line:
                        line_clean = line.strip()
                        output_lines.append(line_clean)
                        print(f"[Config] {line_clean}")
                    else:
                        time.sleep(0.1)
                except:
                    break
            
            # Wait for process to completely finish
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()
            
            success = process.returncode == 0
            elapsed = time.time() - start_time
            
            if success:
                print(f"✅ Language configured in {elapsed:.1f}s")
            else:
                print(f"❌ Return code {process.returncode} after {elapsed:.1f}s")
                # Check if configuration was saved anyway
                config_found = any("pt-BR" in line and "i18n habilitado: True" in line for line in output_lines)
                success_msg_found = any("✅" in line and "Configuração" in line for line in output_lines)
                
                if config_found or success_msg_found:
                    print("ℹ️ But it seems the configuration was saved correctly")
                    success = True  # Consider success if configuration was saved
                else:
                    print("Last lines for debug:")
                    for line in output_lines[-5:]:
                        print(f"  {line}")
                    
            return success
            
        except Exception as e:
            print(f"Configuration error: {e}")
            return False
        finally:
            try:
                os.unlink(config_script)
            except:
                pass
    
    def _run_tutorial_test(self, language_code):
        """
        Second session: Executes the tutorial assuming language is already configured
        
        Args:
            language_code (str): Language code
            
        Returns:
            dict: Test result
        """
        test_script = self._create_tutorial_test_script(language_code)
        
        try:
            # Build Slicer command WITHOUT --testing to allow extensions to load
            # We'll set environment variables instead
            cmd = [str(self.slicer_executable)]
                        
            cmd.extend(['--python-script', test_script])
            
            print(f"Executing tutorial: {' '.join(cmd[:2])} ...")
            print(f"Waiting up to {SLICER_TIMEOUT} seconds...")
            
            start_time = time.time()
            
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                bufsize=1
            )
            
            # Monitor process
            output_lines = []
            last_output_time = time.time()
            download_detected = False
            
            while True:
                if process.poll() is not None:
                    break
                
                elapsed = time.time() - start_time
                time_since_output = time.time() - last_output_time
                
                # Overall timeout
                if elapsed > SLICER_TIMEOUT:
                    print(f"⏰ Overall timeout after {elapsed:.1f}s - terminating process...")
                    process.terminate()
                    try:
                        process.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        process.kill()
                        process.wait()
                    break
                
                try:
                    line = process.stdout.readline()
                    if line:
                        # Handle both text and binary output safely
                        try:
                            if isinstance(line, bytes):
                                line_stripped = line.decode('utf-8', errors='replace').strip()
                            else:
                                line_stripped = line.strip()
                        except Exception as decode_error:
                            # If decoding fails completely, show as hex
                            line_stripped = f"[Binary data: {line[:50]}...]"
                            print(f"⚠️ Decode error: {decode_error}")
                        
                        output_lines.append(line_stripped)
                        print(f"[Tutorial] {line_stripped}")
                        last_output_time = time.time()
                        
                        # Detect downloads (give more time)
                        if 'Downloading' in line_stripped or '.whl' in line_stripped:
                            download_detected = True
                            print(f"📥 Download detected, extending no-output timeout")
                        elif download_detected and ('Successfully installed' in line_stripped or 'Requirement already satisfied' in line_stripped):
                            download_detected = False
                            print(f"✅ Download completed")
                    else:
                        time.sleep(0.1)
                except Exception as e:
                    print(f"Error reading output: {e}")
                    break
            
            # Ensure process is properly terminated
            try:
                process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                print("Process not responding, forcing kill...")
                process.kill()
                process.wait()
            
            return_code = process.returncode
            execution_time = time.time() - start_time
            
            # Better handling of None return code
            if return_code is None:
                print(f"⚠️ Tutorial finished with no return code (process may have crashed) - Time: {execution_time:.1f}s")
                return_code = -999  # Special code for crashed process
            else:
                print(f"Tutorial finished - Code: {return_code}, Time: {execution_time:.1f}s")
            
            # Check result
            result_file = self.output_dir / f"result_{language_code.replace('-', '_')}.json"
            
            # Analyze output for specific errors
            error_hints = []
            if return_code == -999:
                error_hints.append("Process crashed or was killed (no return code)")
            elif return_code == -9:
                error_hints.append("Process was killed with SIGKILL (code -9)")
                error_hints.append("Likely OOM (Out of Memory) or system limit reached")
            elif return_code < 0:
                error_hints.append(f"Process terminated by signal {abs(return_code)}")
            
            # Check for common issues in output
            output_text = '\n'.join(output_lines[-50:])  # Last 50 lines
            if 'MemoryError' in output_text or 'OutOfMemory' in output_text:
                error_hints.append("Out of memory error detected in output")
            if 'No space left' in output_text:
                error_hints.append("Disk space error detected")
            if 'Downloading' in output_text and not any('Successfully installed' in line for line in output_lines[-10:]):
                error_hints.append("Download may have failed or was interrupted")
            if 'Killed' in output_text:
                error_hints.append("Process was killed by system (possibly OOM killer)")
            
            if result_file.exists():
                with open(result_file, 'r', encoding='utf-8') as f:
                    result_data = json.load(f)
                
                result_data['execution_time'] = execution_time
                result_data['return_code'] = return_code
                result_data['slicer_output'] = output_lines[-100:]  # Last 100 lines only
                if error_hints:
                    result_data['error_hints'] = error_hints
                
                return result_data
            else:
                error_msg = f"No result file found. Return code: {return_code}"
                if error_hints:
                    error_msg += f". Possible issues: {', '.join(error_hints)}"
                
                return {
                    "language": language_code,
                    "tutorial": self.tutorial_name,
                    "status": "error",
                    "error": error_msg,
                    "error_hints": error_hints,
                    "slicer_output": output_lines[-100:],  # Last 100 lines only
                    "execution_time": execution_time,
                    "return_code": return_code
                }
                
        except Exception as e:
            return {
                "language": language_code,
                "tutorial": self.tutorial_name,
                "status": "error",
                "error": str(e),
                "execution_time": 0
            }
        finally:
            try:
                os.unlink(test_script)
            except:
                pass
    
    def _create_language_config_script(self, language_code):
        """
        Creates script to ONLY configure the language (first session)
        
        Args:
            language_code (str): Language code
            
        Returns:
            str: Path to temporary script
        """
        script_content = f'''
import slicer
import sys
import time
from datetime import datetime

def log_message(msg):
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{{timestamp}}] {{msg}}")

try:
    log_message("=== Configuring Language ===")
    log_message(f"Target language: {language_code}")
    
    # Wait for initialization
    log_message("Waiting for Slicer initialization...")
    for i in range(3):
        slicer.app.processEvents()
        time.sleep(1)
        log_message(f"Initialization {{i+1}}/3...")
    
    # Configure language
    settings = slicer.app.userSettings()
    original_lang = settings.value('language', 'en-US')
    
    log_message(f"Original language: {{original_lang}}")
    
    settings.setValue('Internationalization/Enabled', True)
    settings.setValue('language', '{language_code}')
    
    log_message("Language preferences saved")
    
    # Try LanguageTools if available
    try:
        from LanguageTools import LanguageToolsLogic
        logic = LanguageToolsLogic()
        logic.enableInternationalization(True)
        log_message("LanguageTools configured")
    except ImportError:
        log_message("LanguageTools not available (OK)")
    
    # Wait for processing
    log_message("Processing settings...")
    for i in range(5):
        slicer.app.processEvents()
        time.sleep(1)
        log_message(f"Processing {{i+1}}/5...")
    
    # Verify configuration
    current_lang = settings.value('language')
    i18n_enabled = settings.value('Internationalization/Enabled')
    
    log_message(f"Final result:")
    log_message(f"  Language: {{current_lang}}")
    log_message(f"  i18n enabled: {{i18n_enabled}}")
    
    if current_lang == '{language_code}':
        log_message("✅ Configuration saved successfully")
        log_message("ℹ️  Language will be applied in next session")
    else:
        log_message("❌ Configuration failed")
        sys.exit(1)
    
    # Explicitly finish
    log_message("Finishing...")
    slicer.app.quit()
    
except Exception as e:
    log_message(f"❌ Erro: {{e}}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
'''
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
            f.write(script_content)
            return f.name
    
    def _create_tutorial_test_script(self, language_code):
        """
        Creates script to execute the tutorial (second session, with language already applied)
        
        Args:
            language_code (str): Language code
            
        Returns:
            str: Path to temporary script
        """
        # Extract tutorial name without ID (part after first underscore)
        tutorial_name_only = self.tutorial_name
        if '_' in tutorial_name_only:
            # Extract name after ID (e.g., "STC-GEN-101_WelcomeTutorial" -> "WelcomeTutorial")
            tutorial_name_only = tutorial_name_only.split('_', 1)[1]
        
        script_content = f'''
import sys
import os
import traceback
import time
import json

# Configure log outputs
log_file = r"{self.output_dir / f"test_{language_code.replace('-', '_')}.log"}"
error_file = r"{self.output_dir / f"error_{language_code.replace('-', '_')}.log"}"

def log_message(message):
    """Log with timestamp"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{{timestamp}}] {{message}}\\n")
    print(f"[{{timestamp}}] {{message}}")

def log_error(message):
    """Error log"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(error_file, "a", encoding="utf-8") as f:
        f.write(f"[{{timestamp}}] {{message}}\\n")
    print(f"[{{timestamp}}] ERROR: {{message}}")

try:
    log_message("=== Executing Tutorial ===")
    log_message(f"Expected language: {language_code}")
    log_message(f"Tutorial: {self.tutorial_name}")
    
    # Set environment variables to indicate CI/testing mode
    # This will be checked by TutorialMaker to skip modal dialogs
    import os
    os.environ['CI'] = 'true'
    os.environ['GITHUB_ACTIONS'] = 'true'
    os.environ['SLICER_TESTING'] = 'true'
    
    # Import Slicer
    import slicer
    log_message("Slicer imported")
    
    # Enable testing mode programmatically (after import)
    # This is safer than using --testing flag which may block extension loading
    if hasattr(slicer.app, 'setTestingEnabled'):
        slicer.app.setTestingEnabled(True)
        log_message("Testing mode enabled programmatically")
    
    # Wait for initialization
    for i in range(3):
        slicer.app.processEvents()
        time.sleep(1)
    
    # Check current language
    settings = slicer.app.userSettings()
    current_lang = settings.value('language')
    i18n_enabled = settings.value('Internationalization/Enabled')
    
    log_message(f"Current language: {{current_lang}}")
    log_message(f"i18n enabled: {{i18n_enabled}}")
    
    if current_lang == '{language_code}':
        log_message("✅ Language applied correctly")
    else:
        log_message(f"⚠️  Different language! Expected: {language_code}, Current: {{current_lang}}")
    
    # List all installed extensions for debugging
    log_message("=== Listing installed Slicer extensions ===")
    try:
        extensionsManagerModel = slicer.app.extensionsManagerModel()
        extensions_path = extensionsManagerModel.extensionsInstallPath()
        log_message(f"Extensions install path: {{extensions_path}}")
        
        installedExtensions = extensionsManagerModel.installedExtensions
        log_message(f"Total installed extensions: {{len(installedExtensions)}}")
        for ext_name in installedExtensions:
            log_message(f"  - {{ext_name}}")
        
        # Also check filesystem
        import os
        if os.path.exists(extensions_path):
            subdirs = [d for d in os.listdir(extensions_path) if os.path.isdir(os.path.join(extensions_path, d))]
            log_message(f"Extension directories found on disk: {{len(subdirs)}}")
            for subdir in subdirs[:5]:
                log_message(f"  - {{subdir}}")
        else:
            log_message(f"Extensions path does not exist: {{extensions_path}}")
            
    except Exception as e:
        log_message(f"Could not list extensions: {{e}}")
        import traceback
        log_message(traceback.format_exc())
    
    # List available modules for debugging
    log_message("=== Listing available modules ===")
    try:
        factory = slicer.app.moduleManager().factoryManager()
        modules = factory.moduleNames()
        log_message(f"Total modules: {{len(modules)}}")
        # Filter to show only relevant modules
        tutorial_modules = [m for m in modules if 'Tutorial' in m or 'Language' in m]
        if tutorial_modules:
            log_message("Tutorial/Language-related modules:")
            for mod in tutorial_modules:
                log_message(f"  - {{mod}}")
        else:
            log_message("No Tutorial/Language modules found")
            log_message("First 10 modules:")
            for mod in list(modules)[:10]:
                log_message(f"  - {{mod}}")
    except Exception as e:
        log_message(f"Could not list modules: {{e}}")
    
    # Load TutorialMaker
    log_message("Loading TutorialMaker...")
    
    try:
        from TutorialMaker import TutorialMakerLogic
        slicer.mrmlScene.Clear()

        slicer.util.mainWindow().resize(1920, 1080)

        appFont = slicer.app.font()
        appFont.setPointSize(14)
        slicer.app.setFont(appFont)
        
        # Verify tutorial files are in place
        log_message(f"Checking tutorial setup for: {tutorial_name_only}")
        
        # Import necessary libraries
        from pathlib import Path
        
        # Find TutorialMaker directory using Slicer's API
        log_message("Locating TutorialMaker extension directory...")
        try:
            # Use slicer.util.modulePath to get the actual installed path
            tutorialmaker_module_path = slicer.util.modulePath("TutorialMaker")
            tutorialmaker_dir = Path(tutorialmaker_module_path).parent
            log_message(f"TutorialMaker found at: {{tutorialmaker_dir}}")
        except Exception as e:
            log_message(f"Error getting TutorialMaker path: {{e}}")
            raise Exception("TutorialMaker extension not found. Make sure it's installed.")
        
        # Check annotations directory for this tutorial
        annotations_dir = tutorialmaker_dir / "Outputs" / "Annotations" / "{tutorial_name_only}"
        log_message(f"Annotations directory: {{annotations_dir}}")
        log_message(f"Annotations directory exists: {{annotations_dir.exists()}}")
        
        # List existing files in directory for debug
        if annotations_dir.exists():
            existing_files = list(annotations_dir.glob("*.json"))
            log_message(f"JSON files found in annotations directory: {{len(existing_files)}}")
            for file in existing_files:
                log_message(f"  - {{file.name}}")
        else:
            log_message(f"⚠️ WARNING: Annotations directory does not exist!")
        
        # Check Testing directory
        testing_dir = tutorialmaker_dir / "Testing"
        if testing_dir.exists():
            py_files = list(testing_dir.glob("{tutorial_name_only}.py"))
            log_message(f"Tutorial Python file in Testing: {{'Found' if py_files else 'NOT FOUND'}}")
        else:
            log_message(f"⚠️ WARNING: Testing directory does not exist!")
        
        # Select module
        slicer.util.moduleSelector().selectModule('TutorialMaker')
        time.sleep(2)
        slicer.app.processEvents()
        
        log_message("TutorialMaker loaded successfully")
        
        # Global variables for control
        global test_completed, test_success
        test_completed = False
        test_success = False
        
        def finish_callback():
            global test_completed, test_success
            log_message("📞 Finish callback called!")
            test_completed = True
            test_success = True
            log_message(f"Tutorial {self.tutorial_name} finished successfully")
        
        # Execute tutorial
        log_message(f"Starting tutorial: {tutorial_name_only} (Full ID/name: {self.tutorial_name})")
        
        TutorialMakerLogic.runTutorialTestCases('{tutorial_name_only}', finish_callback)
        
        # Wait for completion with more aggressive event processing
        timeout_counter = 0
        max_timeout = {SLICER_TIMEOUT}
        
        while not test_completed and timeout_counter < max_timeout:
            # Process events more frequently to ensure Qt timers fire
            for _ in range(10):
                slicer.app.processEvents()
            time.sleep(0.1)
            timeout_counter += 1
            
            # Log progress every 30 seconds
            if timeout_counter % 300 == 0:  # Every 30s (300 * 0.1s)
                log_message(f"Tutorial running... {{timeout_counter//10}}/{{max_timeout}}s")
        
        if not test_completed:
            raise Exception(f"Tutorial did not complete in {{max_timeout}} seconds")
        
        if not test_success:
            raise Exception("Tutorial failed during execution")
        
        # Generate tutorial outputs using TutorialMaker
        log_message("Generating tutorial outputs...")
        generation_success = False
        
        try:
            # Get TutorialMaker logic
            logic = slicer.util.getModuleLogic("TutorialMaker")
            if logic and hasattr(logic, 'Generate'):
                log_message(f"Calling Generate for tutorial: {tutorial_name_only} (Full name: {self.tutorial_name})")
                
                # Set CI environment variable to prevent modal dialogs
                os.environ['CI'] = 'true'
                os.environ['GITHUB_ACTIONS'] = 'true'
                
                log_message("=== Calling Generate ===")
                
                # Call Generate directly (no threading - Qt doesn't allow UI operations in threads)
                try:
                    logic.Generate('{tutorial_name_only}')
                    generation_success = True
                    log_message("✅ Outputs generated successfully")
                except Exception as e:
                    log_message(f"❌ Error during Generate: {{e}}")
                    import traceback
                    log_message(traceback.format_exc())
                    generation_success = False
                
            else:
                log_message("⚠️  Generate method not found in TutorialMaker logic")
                log_message("Skipping output generation")
                
        except Exception as e:
            log_error(f"Error in generation: {{e}}")
            import traceback
            log_error(traceback.format_exc())
            # Generation error is not fatal
            log_message("Continuing despite generation error...")
        
        # Always save success result (generation is optional)
        log_message("Saving test results...")
        
        # Save success result
        result_data = {{
            "language": "{language_code}",
            "tutorial": "{self.tutorial_name}",
            "status": "success",
            "timestamp": time.time(),
            "final_language": settings.value('language'),
            "generation_success": generation_success
        }}
        
        result_file = r"{self.output_dir / f"result_{language_code.replace('-', '_')}.json"}"
        with open(result_file, "w", encoding="utf-8") as f:
            json.dump(result_data, f, indent=2)
        
        log_message("✅ TUTORIAL EXECUTED SUCCESSFULLY")
        
    except ImportError as e:
        log_error(f"TutorialMaker not found: {{e}}")
        raise
    except Exception as e:
        log_error(f"Error in tutorial: {{e}}")
        raise

except Exception as e:
    log_error(f"General error: {{e}}")
    log_error(traceback.format_exc())
    
    # Save error result
    try:
        result_data = {{
            "language": "{language_code}",
            "tutorial": "{self.tutorial_name}",
            "status": "error",
            "error": str(e),
            "timestamp": time.time()
        }}
        
        result_file = r"{self.output_dir / f"result_{language_code.replace('-', '_')}.json"}"
        with open(result_file, "w", encoding="utf-8") as f:
            json.dump(result_data, f, indent=2)
    except:
        pass
    
    log_error("❌ TUTORIAL FALHOU")
    
    # Exit with error code using Slicer's proper exit
    try:
        slicer.util.exit(1)
    except:
        sys.exit(1)

# Success - exit gracefully
log_message("Script finalizado normalmente")
log_message("Fechando Slicer...")

# Use Slicer's proper exit method to avoid "exit abnormally" messages
try:
    # Process any remaining events
    for _ in range(10):
        slicer.app.processEvents()
    time.sleep(0.5)
    
    # Exit cleanly using Slicer's method
    slicer.util.exit(0)
except:
    # Fallback to normal exit
    sys.exit(0)
'''
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
            f.write(script_content)
            return f.name
    
    def run_all_tests(self, language_codes=None):
        """
        Runs tests for all languages
        
        Args:
            language_codes (list): List of language codes
            
        Returns:
            dict: Results of all tests
        """
        if language_codes is None:
            language_codes = DEFAULT_LANGUAGES
        
        print(f"Running tests for languages: {', '.join(language_codes)}")
        print(f"Tutorial: {self.tutorial_name}")
        print(f"Slicer: {self.slicer_executable}")
        print(f"Output: {self.output_dir}")
        
        results = {}
        
        for lang in language_codes:
            try:
                result = self.run_test_for_language(lang)
                results[lang] = result
                
                # Log result
                status = result.get('status', 'unknown')
                exec_time = result.get('execution_time', 0)
                
                if status == 'success':
                    print(f"✅ {lang}: SUCCESS ({exec_time:.1f}s)")
                elif status == 'timeout':
                    print(f"⏰ {lang}: TIMEOUT ({exec_time:.1f}s)")
                else:
                    error = result.get('error', 'Unknown error')
                    print(f"❌ {lang}: ERROR - {error}")
                    
            except Exception as e:
                print(f"💥 {lang}: EXCEPTION - {str(e)}")
                results[lang] = {
                    "language": lang,
                    "status": "exception",
                    "error": str(e)
                }
        
        return results
    
    def generate_report(self, results):
        """
        Generates final test report
        
        Args:
            results (dict): Test results
            
        Returns:
            dict: Consolidated report
        """
        total_tests = len(results)
        successful_tests = sum(1 for r in results.values() if r.get('status') == 'success')
        
        report = {
            "tutorial": self.tutorial_name,
            "timestamp": time.time(),
            "summary": {
                "total_tests": total_tests,
                "successful_tests": successful_tests,
                "failed_tests": total_tests - successful_tests,
                "success_rate": (successful_tests / total_tests * 100) if total_tests > 0 else 0
            },
            "results": results
        }
        
        # Save report
        report_file = self.output_dir / "test_report.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        
        # Console report
        print("\\n" + "="*60)
        print("FINAL REPORT")
        print("="*60)
        print(f"Tutorial: {self.tutorial_name}")
        print(f"Total tests: {total_tests}")
        print(f"Successes: {successful_tests}")
        print(f"Failures: {total_tests - successful_tests}")
        print(f"Success rate: {report['summary']['success_rate']:.1f}%")
        print()
        
        for lang, result in results.items():
            status = result.get('status', 'unknown')
            exec_time = result.get('execution_time', 0)
            
            status_icon = {
                'success': '✅',
                'error': '❌',
                'timeout': '⏰',
                'exception': '💥'
            }.get(status, '❓')
            
            print(f"{status_icon} {lang:8}: {status.upper():<10} ({exec_time:.1f}s)")
            
            if status != 'success' and 'error' in result:
                print(f"    └─ {result['error']}")
        
        print("\\nReport saved at:", report_file)
        
        return report

def main():
    """Main function for command-line usage"""
    global SLICER_TIMEOUT
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Runs TutorialMaker tests in multiple languages for CI'
    )
    parser.add_argument('slicer_path', help='Path to Slicer executable')
    parser.add_argument('--tutorial', default='TestTutorial', help='Tutorial name to test')
    parser.add_argument('--languages', nargs='+', default=DEFAULT_LANGUAGES, 
                       help='List of languages to test')
    parser.add_argument('--output', help='Output directory for logs and reports')
    parser.add_argument('--timeout', type=int, default=SLICER_TIMEOUT, 
                       help='Timeout in seconds per test')
    
    args = parser.parse_args()
    
    # Validate Slicer executable
    if not os.path.exists(args.slicer_path):
        print(f"ERROR: Slicer executable not found: {args.slicer_path}")
        sys.exit(1)
    
    # Update global timeout
    SLICER_TIMEOUT = args.timeout
    
    # Create runner
    runner = TutorialTestRunner(
        slicer_executable=args.slicer_path,
        tutorial_name=args.tutorial,
        output_dir=args.output
    )
    
    try:
        # Run tests
        results = runner.run_all_tests(args.languages)
        
        # Generate report
        report = runner.generate_report(results)
        
        # Determine exit code
        success_rate = report['summary']['success_rate']
        
        if success_rate == 100:
            print("\\n🎉 All tests passed!")
            sys.exit(0)
        elif success_rate >= 50:
            print(f"\\n⚠️  Some tests failed ({success_rate:.1f}% success)")
            sys.exit(1)
        else:
            print(f"\\n💀 Many tests failed ({success_rate:.1f}% success)")
            sys.exit(2)
            
    except Exception as e:
        print(f"\\n💥 FATAL ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(3)

if __name__ == "__main__":
    main()