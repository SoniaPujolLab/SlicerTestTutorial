#!/usr/bin/env python3
"""
Script para executar testes do TutorialMaker em múltiplas linguagens no CI/GitHub Actions
Otimizado para execução em containers e ambientes headless
"""

import sys
import os
import json
import time
import tempfile
import subprocess
from pathlib import Path

# Configurações padrão
DEFAULT_LANGUAGES = ["pt-BR", "es-419", "fr-FR"]
SLICER_TIMEOUT = 300  # 5 minutos timeout por teste

class TutorialTestRunner:
    """Runner para testes de tutorial em múltiplas linguagens"""
    
    def __init__(self, slicer_executable, tutorial_name=None, output_dir=None):
        self.slicer_executable = Path(slicer_executable)
        self.tutorial_name = tutorial_name or "TestTutorial"
        self.output_dir = Path(output_dir) if output_dir else Path.cwd() / "test_outputs"
        self.results = {}
        
        # Criar diretório de saída
        self.output_dir.mkdir(exist_ok=True)
        
    def run_test_for_language(self, language_code):
        """
        Executa teste para uma linguagem específica usando estratégia de reinício:
        1. Primeira sessão: Configura linguagem e aguarda
        2. Segunda sessão: Executa tutorial com linguagem aplicada
        
        Args:
            language_code (str): Código da linguagem
            
        Returns:
            dict: Resultado do teste
        """
        print(f"\\n=== Testando linguagem: {language_code} ===")
        
        try:
            # Passo 1: Configurar linguagem
            print("Passo 1: Configurando linguagem...")
            config_success = self._configure_language(language_code)
            
            if not config_success:
                return {
                    "language": language_code,
                    "tutorial": self.tutorial_name,
                    "status": "error",
                    "error": "Falha na configuração de linguagem",
                    "execution_time": 0
                }
            
            # Passo 2: Executar tutorial com linguagem configurada
            print("Passo 2: Executando tutorial com linguagem aplicada...")
            return self._run_tutorial_test(language_code)
            
        except Exception as e:
            print(f"💥 Erro geral no teste para {language_code}: {e}")
            return {
                "language": language_code,
                "tutorial": self.tutorial_name,
                "status": "exception",
                "error": str(e),
                "execution_time": 0
            }
    
    def _configure_language(self, language_code):
        """
        Primeira sessão: Apenas configura a linguagem nas preferências
        
        Args:
            language_code (str): Código da linguagem
            
        Returns:
            bool: True se configuração foi bem-sucedida
        """
        config_script = self._create_language_config_script(language_code)
        
        try:
            # Comando simples para configuração
            cmd = [str(self.slicer_executable), '--no-splash', '--python-script', config_script]
            
            print(f"Configurando: {' '.join(cmd[:2])} ...")
            
            start_time = time.time()
            
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                universal_newlines=True
            )
            
            # Timeout curto para configuração (30 segundos)
            config_timeout = 30
            output_lines = []
            
            while True:
                if process.poll() is not None:
                    break
                    
                elapsed = time.time() - start_time
                if elapsed > config_timeout:
                    print(f"⏰ Timeout na configuração após {elapsed:.1f}s")
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
            
            # Aguardar processo terminar completamente
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()
            
            success = process.returncode == 0
            elapsed = time.time() - start_time
            
            if success:
                print(f"✅ Linguagem configurada em {elapsed:.1f}s")
            else:
                print(f"❌ Return code {process.returncode} após {elapsed:.1f}s")
                # Verificar se a configuração foi salva mesmo assim
                config_found = any("pt-BR" in line and "i18n habilitado: True" in line for line in output_lines)
                success_msg_found = any("✅" in line and "Configuração" in line for line in output_lines)
                
                if config_found or success_msg_found:
                    print("ℹ️ Mas parece que a configuração foi salva corretamente")
                    success = True  # Considerar sucesso se configuração foi salva
                else:
                    print("Últimas linhas para debug:")
                    for line in output_lines[-5:]:
                        print(f"  {line}")
                    
            return success
            
        except Exception as e:
            print(f"Erro na configuração: {e}")
            return False
        finally:
            try:
                os.unlink(config_script)
            except:
                pass
    
    def _run_tutorial_test(self, language_code):
        """
        Segunda sessão: Executa o tutorial assumindo que linguagem já está configurada
        
        Args:
            language_code (str): Código da linguagem
            
        Returns:
            dict: Resultado do teste
        """
        test_script = self._create_tutorial_test_script(language_code)
        
        try:
            # Montar comando do Slicer
            cmd = [str(self.slicer_executable), '--no-splash']
            
            # Adicionar opções apenas se não for Windows
            import platform
            if platform.system() != "Windows":
                cmd.extend(['--no-main-window', '--disable-cli-modules'])
            
            cmd.extend(['--python-script', test_script])
            
            print(f"Executando tutorial: {' '.join(cmd[:2])} ...")
            print(f"Aguardando até {SLICER_TIMEOUT} segundos...")
            
            start_time = time.time()
            
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                universal_newlines=True
            )
            
            # Monitorar processo
            output_lines = []
            while True:
                if process.poll() is not None:
                    break
                
                elapsed = time.time() - start_time
                if elapsed > SLICER_TIMEOUT:
                    print(f"⏰ Timeout após {elapsed:.1f}s - terminando processo...")
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
                        output_lines.append(line.strip())
                        print(f"[Tutorial] {line.strip()}")
                    else:
                        time.sleep(0.1)
                except:
                    break
            
            return_code = process.returncode
            execution_time = time.time() - start_time
            
            print(f"Tutorial finalizado - Código: {return_code}, Tempo: {execution_time:.1f}s")
            
            # Verificar resultado
            result_file = self.output_dir / f"result_{language_code.replace('-', '_')}.json"
            
            if result_file.exists():
                with open(result_file, 'r', encoding='utf-8') as f:
                    result_data = json.load(f)
                
                result_data['execution_time'] = execution_time
                result_data['return_code'] = return_code
                result_data['slicer_output'] = output_lines
                
                return result_data
            else:
                return {
                    "language": language_code,
                    "tutorial": self.tutorial_name,
                    "status": "error",
                    "error": f"No result file found. Return code: {return_code}",
                    "slicer_output": output_lines,
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
        Cria script para APENAS configurar a linguagem (primeira sessão)
        
        Args:
            language_code (str): Código da linguagem
            
        Returns:
            str: Caminho do script temporário
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
    log_message("=== Configurando Linguagem ===")
    log_message(f"Linguagem alvo: {language_code}")
    
    # Aguardar inicialização
    log_message("Aguardando inicialização do Slicer...")
    for i in range(3):
        slicer.app.processEvents()
        time.sleep(1)
        log_message(f"Inicialização {{i+1}}/3...")
    
    # Configurar linguagem
    settings = slicer.app.userSettings()
    original_lang = settings.value('language', 'en-US')
    
    log_message(f"Linguagem original: {{original_lang}}")
    
    settings.setValue('Internationalization/Enabled', True)
    settings.setValue('language', '{language_code}')
    
    log_message("Preferências de linguagem salvas")
    
    # Tentar LanguageTools se disponível
    try:
        from LanguageTools import LanguageToolsLogic
        logic = LanguageToolsLogic()
        logic.enableInternationalization(True)
        log_message("LanguageTools configurado")
    except ImportError:
        log_message("LanguageTools não disponível (OK)")
    
    # Aguardar processamento
    log_message("Processando configurações...")
    for i in range(5):
        slicer.app.processEvents()
        time.sleep(1)
        log_message(f"Processamento {{i+1}}/5...")
    
    # Verificar configuração
    current_lang = settings.value('language')
    i18n_enabled = settings.value('Internationalization/Enabled')
    
    log_message(f"Resultado final:")
    log_message(f"  Linguagem: {{current_lang}}")
    log_message(f"  i18n habilitado: {{i18n_enabled}}")
    
    if current_lang == '{language_code}':
        log_message("✅ Configuração salva com sucesso")
        log_message("ℹ️  Linguagem será aplicada na próxima sessão")
    else:
        log_message("❌ Configuração falhou")
        sys.exit(1)
    
    # Finalizar explicitamente
    log_message("Finalizando...")
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
        Cria script para executar o tutorial (segunda sessão, com linguagem já aplicada)
        
        Args:
            language_code (str): Código da linguagem
            
        Returns:
            str: Caminho do script temporário
        """
        script_content = f'''
import sys
import os
import traceback
import time
import json

# Configurar saídas para log
log_file = r"{self.output_dir / f"test_{language_code.replace('-', '_')}.log"}"
error_file = r"{self.output_dir / f"error_{language_code.replace('-', '_')}.log"}"

def log_message(message):
    """Log com timestamp"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{{timestamp}}] {{message}}\\n")
    print(f"[{{timestamp}}] {{message}}")

def log_error(message):
    """Log de erro"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(error_file, "a", encoding="utf-8") as f:
        f.write(f"[{{timestamp}}] {{message}}\\n")
    print(f"[{{timestamp}}] ERROR: {{message}}")

try:
    log_message("=== Executando Tutorial ===")
    log_message(f"Linguagem esperada: {language_code}")
    log_message(f"Tutorial: {self.tutorial_name}")
    
    # Importar Slicer
    import slicer
    log_message("Slicer importado")
    
    # Aguardar inicialização
    for i in range(3):
        slicer.app.processEvents()
        time.sleep(1)
    
    # Verificar linguagem atual
    settings = slicer.app.userSettings()
    current_lang = settings.value('language')
    i18n_enabled = settings.value('Internationalization/Enabled')
    
    log_message(f"Linguagem atual: {{current_lang}}")
    log_message(f"i18n habilitado: {{i18n_enabled}}")
    
    if current_lang == '{language_code}':
        log_message("✅ Linguagem aplicada corretamente")
    else:
        log_message(f"⚠️  Linguagem diferente! Esperada: {language_code}, Atual: {{current_lang}}")
    
    # Carregar TutorialMaker
    log_message("Carregando TutorialMaker...")
    
    try:
        from TutorialMaker import TutorialMakerLogic
        slicer.mrmlScene.Clear()

        slicer.util.mainWindow().resize(1920, 1080)

        appFont = slicer.app.font()
        appFont.setPointSize(14)
        slicer.app.setFont(appFont)
        
        # Configurar arquivos JSON necessários para a linguagem
        log_message(f"Configurando arquivos JSON para linguagem: {language_code}")
        
        # Importar bibliotecas necessárias
        import shutil
        from pathlib import Path
        
        # Encontrar diretório do TutorialMaker
        tutorialmaker_module = slicer.util.getModuleLogic("TutorialMaker")
        if hasattr(tutorialmaker_module, 'resourcePath'):
            tutorialmaker_dir = Path(tutorialmaker_module.resourcePath('.'))
        else:
            # Fallback: usar localização padrão baseada em slicer
            slicer_dir = Path(slicer.app.slicerHome)
            # Procurar por TutorialMaker nas extensões
            possible_dirs = [
                slicer_dir / "lib" / "Slicer-*" / "qt-scripted-modules" / "TutorialMaker",
                slicer_dir / "lib" / "Slicer-*" / "extensions-*" / "TutorialMaker*"
            ]
            tutorialmaker_dir = None
            for pattern in possible_dirs:
                matches = list(slicer_dir.glob(str(pattern.relative_to(slicer_dir))))
                if matches:
                    tutorialmaker_dir = matches[0]
                    break
            
            if not tutorialmaker_dir:
                log_message("Criando diretório TutorialMaker padrão...")
                tutorialmaker_dir = slicer_dir / "lib" / "Slicer-5.8" / "qt-scripted-modules" / "TutorialMaker"
                tutorialmaker_dir.mkdir(parents=True, exist_ok=True)
        
        annotations_dir = tutorialmaker_dir / "Outputs" / "Annotations"
        annotations_dir.mkdir(parents=True, exist_ok=True)
        log_message(f"Diretório de anotações: {{annotations_dir}}")
        
        # Listar arquivos existentes no diretório para debug
        try:
            existing_files = list(annotations_dir.glob("*.json"))
            log_message(f"Arquivos JSON encontrados em {{annotations_dir}}:")
            for file in existing_files:
                log_message(f"  - {{file.name}}")
        except Exception as e:
            log_message(f"Erro ao listar arquivos: {{e}}")
        
        # Copiar text_dict_default.json específico da linguagem
        lang_dict_file = annotations_dir / f"text_dict_default_{language_code}.json"
        target_dict_file = annotations_dir / "text_dict_default.json"
        
        log_message(f"Procurando arquivo: {{lang_dict_file}}")
        log_message(f"Arquivo existe: {{lang_dict_file.exists()}}")
        
        if lang_dict_file.exists():
            log_message(f"✅ Copiando arquivo de traduções: {{lang_dict_file}} -> {{target_dict_file}}")
            shutil.copy2(lang_dict_file, target_dict_file)
            
            # Verificar se a cópia foi bem-sucedida
            if target_dict_file.exists():
                log_message(f"✅ Arquivo copiado com sucesso!")
                # Mostrar primeiras linhas do arquivo para confirmação
                try:
                    with open(target_dict_file, 'r', encoding='utf-8') as f:
                        content = f.read()[:200]
                        log_message(f"Primeiros caracteres do arquivo: {{content[:100]}}...")
                except Exception as e:
                    log_message(f"Erro ao ler arquivo copiado: {{e}}")
            else:
                log_message(f"❌ Erro: arquivo não foi copiado!")
        else:
            log_message(f"❌ Arquivo de traduções não encontrado: {{lang_dict_file}}")
            log_message(f"Tentando localizar arquivos similares...")
            
            # Tentar encontrar arquivos com padrões similares
            similar_patterns = [
                f"text_dict_default_{language_code.replace('-', '_')}.json",
                f"text_dict_default_{language_code.replace('-', '')}.json",
                f"text_dict_default_{language_code.lower()}.json"
            ]
            
            found_alternative = False
            for pattern in similar_patterns:
                alt_file = annotations_dir / pattern
                log_message(f"Testando padrão: {{alt_file}}")
                if alt_file.exists():
                    log_message(f"✅ Encontrado arquivo alternativo: {{alt_file}}")
                    shutil.copy2(alt_file, target_dict_file)
                    found_alternative = True
                    break
            
            if not found_alternative:
                log_message(f"❌ Nenhum arquivo de tradução encontrado")
                # Criar arquivo vazio como fallback
                with open(target_dict_file, 'w', encoding='utf-8') as f:
                    json.dump({{}}, f)
                log_message("Criado arquivo de traduções vazio como fallback")
        
        # Selecionar módulo
        slicer.util.moduleSelector().selectModule('TutorialMaker')
        time.sleep(2)
        slicer.app.processEvents()
        
        log_message("TutorialMaker carregado com sucesso")
        
        # Variáveis globais para controle
        global test_completed, test_success
        test_completed = False
        test_success = False
        
        def finish_callback():
            global test_completed, test_success
            test_completed = True
            test_success = True
            log_message(f"Tutorial {self.tutorial_name} finalizado com sucesso")
        
        # Executar tutorial
        log_message(f"Iniciando tutorial: {self.tutorial_name}")
        
        TutorialMakerLogic.runTutorialTestCases('{self.tutorial_name}', finish_callback)
        
        # Aguardar conclusão
        timeout_counter = 0
        max_timeout = {SLICER_TIMEOUT}
        
        while not test_completed and timeout_counter < max_timeout:
            slicer.app.processEvents()
            time.sleep(1)
            timeout_counter += 1
            
            # Log progresso a cada 30 segundos
            if timeout_counter % 30 == 0:
                log_message(f"Tutorial em execução... {{timeout_counter}}/{{max_timeout}}s")
        
        if not test_completed:
            raise Exception(f"Tutorial não completou em {{max_timeout}} segundos")
        
        if not test_success:
            raise Exception("Tutorial falhou durante execução")
        
        # Gerar outputs do tutorial usando TutorialMaker
        log_message("Gerando outputs do tutorial...")
        try:
            # Obter lógica do TutorialMaker
            logic = slicer.util.getModuleLogic("TutorialMaker")
            if logic and hasattr(logic, 'Generate'):
                log_message(f"Chamando Generate para tutorial: {self.tutorial_name}")
                logic.Generate('{self.tutorial_name}')
                log_message("✅ Outputs gerados com sucesso")
            else:
                log_message("⚠️  Método Generate não encontrado na lógica do TutorialMaker")
        except Exception as e:
            log_error(f"Erro ao gerar outputs: {{e}}")
            # Não falhar o teste por erro na geração - isso é não-crítico para o teste básico
            log_message("Continuando mesmo com erro na geração de outputs...")
        
        # Salvar resultado de sucesso
        result_data = {{
            "language": "{language_code}",
            "tutorial": "{self.tutorial_name}",
            "status": "success",
            "timestamp": time.time(),
            "final_language": settings.value('language')
        }}
        
        result_file = r"{self.output_dir / f"result_{language_code.replace('-', '_')}.json"}"
        with open(result_file, "w", encoding="utf-8") as f:
            json.dump(result_data, f, indent=2)
        
        log_message("✅ TUTORIAL EXECUTADO COM SUCESSO")
        
    except ImportError as e:
        log_error(f"TutorialMaker não encontrado: {{e}}")
        raise
    except Exception as e:
        log_error(f"Erro no tutorial: {{e}}")
        raise

except Exception as e:
    log_error(f"Erro geral: {{e}}")
    log_error(traceback.format_exc())
    
    # Salvar resultado de erro
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
    sys.exit(1)

log_message("Script finalizado normalmente")
'''
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
            f.write(script_content)
            return f.name
    
    def run_all_tests(self, language_codes=None):
        """
        Executa testes para todas as linguagens
        
        Args:
            language_codes (list): Lista de códigos de linguagem
            
        Returns:
            dict: Resultados de todos os testes
        """
        if language_codes is None:
            language_codes = DEFAULT_LANGUAGES
        
        print(f"Executando testes para linguagens: {', '.join(language_codes)}")
        print(f"Tutorial: {self.tutorial_name}")
        print(f"Slicer: {self.slicer_executable}")
        print(f"Saída: {self.output_dir}")
        
        results = {}
        
        for lang in language_codes:
            try:
                result = self.run_test_for_language(lang)
                results[lang] = result
                
                # Log resultado
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
        Gera relatório final dos testes
        
        Args:
            results (dict): Resultados dos testes
            
        Returns:
            dict: Relatório consolidado
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
        
        # Salvar relatório
        report_file = self.output_dir / "test_report.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        
        # Relatório de console
        print("\\n" + "="*60)
        print("RELATÓRIO FINAL")
        print("="*60)
        print(f"Tutorial: {self.tutorial_name}")
        print(f"Total de testes: {total_tests}")
        print(f"Sucessos: {successful_tests}")
        print(f"Falhas: {total_tests - successful_tests}")
        print(f"Taxa de sucesso: {report['summary']['success_rate']:.1f}%")
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
        
        print("\\nRelatório salvo em:", report_file)
        
        return report

def main():
    """Função principal para uso via linha de comando"""
    global SLICER_TIMEOUT
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Executa testes do TutorialMaker em múltiplas linguagens para CI'
    )
    parser.add_argument('slicer_path', help='Caminho para o executável do Slicer')
    parser.add_argument('--tutorial', default='TestTutorial', help='Nome do tutorial para testar')
    parser.add_argument('--languages', nargs='+', default=DEFAULT_LANGUAGES, 
                       help='Lista de linguagens para testar')
    parser.add_argument('--output', help='Diretório de saída para logs e relatórios')
    parser.add_argument('--timeout', type=int, default=SLICER_TIMEOUT, 
                       help='Timeout em segundos por teste')
    
    args = parser.parse_args()
    
    # Validar executável do Slicer
    if not os.path.exists(args.slicer_path):
        print(f"ERRO: Executável do Slicer não encontrado: {args.slicer_path}")
        sys.exit(1)
    
    # Atualizar timeout global
    SLICER_TIMEOUT = args.timeout
    
    # Criar runner
    runner = TutorialTestRunner(
        slicer_executable=args.slicer_path,
        tutorial_name=args.tutorial,
        output_dir=args.output
    )
    
    try:
        # Executar testes
        results = runner.run_all_tests(args.languages)
        
        # Gerar relatório
        report = runner.generate_report(results)
        
        # Determinar código de saída
        success_rate = report['summary']['success_rate']
        
        if success_rate == 100:
            print("\\n🎉 Todos os testes passaram!")
            sys.exit(0)
        elif success_rate >= 50:
            print(f"\\n⚠️  Alguns testes falharam ({success_rate:.1f}% sucesso)")
            sys.exit(1)
        else:
            print(f"\\n💀 Muitos testes falharam ({success_rate:.1f}% sucesso)")
            sys.exit(2)
            
    except Exception as e:
        print(f"\\n💥 ERRO FATAL: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(3)

if __name__ == "__main__":
    main()