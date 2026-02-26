import json
import os
import argparse
import re
import tempfile
import subprocess
import xml.etree.ElementTree as ET

# ------------------------
# Parsing Utilities
# ------------------------
def parse_filename_language(filename):
    base = os.path.splitext(os.path.basename(filename))[0]
    match = re.match(r"(.+)_([a-z]{2}(?:-[A-Z]{2})?)$", base)
    if match:
        context = match.group(1)
        language = match.group(2)
    else:
        context = base
        language = "en-US"
    return context, language

def load_existing_translations(ts_path):
    """Load existing translations from a TS file to preserve them"""
    if not os.path.exists(ts_path):
        return {}
    try:
        tree = ET.parse(ts_path)
        root = tree.getroot()
        translations = {}
        for context in root.findall("context"):
            for message in context.findall("message"):
                extracomment_elem = message.find("extracomment")
                source_elem = message.find("source")
                translation_elem = message.find("translation")
                
                if extracomment_elem is not None and source_elem is not None:
                    key = extracomment_elem.text
                    source_text = source_elem.text
                    
                    if translation_elem is not None and translation_elem.get("type") != "unfinished":
                        translation_text = translation_elem.text or ""
                        translations[key] = (source_text, translation_text)
        
        return translations
    except Exception as e:
        print(f"Warning: Could not load existing translations from {ts_path}: {e}")
        return {}

# ------------------------
# JSON -> temporary .cpp
# ------------------------
def json_to_temp_cpp(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    json_filename = os.path.basename(json_path)
    json_basename = os.path.splitext(json_filename)[0]
    
    lines = []
    lines.append('#include <QObject>\n\n')
    lines.append('class Main : public QObject {\n')
    lines.append('    Q_OBJECT\n')
    lines.append('public:\n')
    lines.append('    void main() {\n')

    line_number = 6  # Starting line number for tr() calls

    def add_lines(obj, path=""):
        nonlocal line_number
        if isinstance(obj, dict):
            for k, v in obj.items():
                new_path = f"{path}.{k}" if path else k
                add_lines(v, new_path)
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                new_path = f"{path}[{i}]"
                add_lines(v, new_path)
        elif isinstance(obj, str):
            # Only process non-empty strings
            if obj.strip():
                safe_text = obj.replace('"', '\\"').replace('\n', '\\n')
                # Use the JSON path as translator comment for Qt's translation system
                lines.append(f'        //: {path}\n')
                lines.append(f'        tr("{safe_text}");\n')
                line_number += 1

    add_lines(data)

    lines.append('    }\n')
    lines.append('};\n')

    # Create temporary file with a name similar to the JSON file
    temp_dir = tempfile.gettempdir()
    temp_filename = f"{json_basename}_temp.cpp"
    temp_path = os.path.join(temp_dir, temp_filename)
    
    with open(temp_path, "w", encoding="utf-8") as tmp:
        tmp.writelines(lines)

    print(f"Temporary C++ file created: {temp_path}")
    return temp_path

# ------------------------
# Manual TS generation (fallback when lupdate is not available)
# ------------------------
def create_ts_manually(temp_cpp, ts_output, language="en-US", context_name="TutorialMaker", original_json_path=None):
    """Create TS file manually by parsing the temporary C++ file"""
    
    # Load existing translations to preserve them
    existing_translations = load_existing_translations(ts_output)
    
    with open(temp_cpp, 'r', encoding='utf-8') as f:
        cpp_content = f.read()
    
    # Extract translation strings and their keys
    translations = []
    lines = cpp_content.split('\n')
    
    line_number = 1
    json_filename = os.path.basename(original_json_path) if original_json_path else "unknown.json"
    
    for i, line in enumerate(lines):
        if line.strip().startswith('//:'): 
            # Get the JSON key from the comment
            json_key = line.strip()[3:].strip()
            # Get the next line which should contain the tr() call
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if next_line.startswith('tr("') and next_line.endswith('");'):
                    # Extract the text from tr("text");
                    tr_text = next_line[4:-3]  # Remove tr(" and ");
                    # Unescape the text
                    tr_text = tr_text.replace('\\"', '"').replace('\\n', '\n')
                    translations.append((json_key, tr_text, line_number))
                    line_number += 1
    
    # Create TS XML content
    # Keep the language code as-is (use hyphen, don't convert to underscore)
    lang_code = language
    ts_content = f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="{lang_code}">
<context>
    <name>{context_name}</name>
'''
    
    for json_key, text, line_num in translations:
        # Escape XML characters
        escaped_text = (text.replace('&', '&amp;')
                           .replace('<', '&lt;')
                           .replace('>', '&gt;')
                           .replace('"', '&quot;')
                           .replace("'", '&apos;'))
        
        # Check if we have an existing translation
        translation_text = ""
        translation_type = "unfinished"
        
        if json_key in existing_translations:
            stored_source, stored_translation = existing_translations[json_key]
            # Only preserve translation if source text hasn't changed
            if stored_source == text and stored_translation:
                translation_text = stored_translation.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&apos;')
                translation_type = "finished"
        
        if translation_text:
            ts_content += f'''    <message>
        <location filename="{json_filename}" line="{line_num}"/>
        <source>{escaped_text}</source>
        <extracomment>{json_key}</extracomment>
        <translation type="{translation_type}">{translation_text}</translation>
    </message>
'''
        else:
            ts_content += f'''    <message>
        <location filename="{json_filename}" line="{line_num}"/>
        <source>{escaped_text}</source>
        <extracomment>{json_key}</extracomment>
        <translation type="unfinished"></translation>
    </message>
'''
    
    ts_content += '''</context>
</TS>
'''
    
    # Write the TS file
    with open(ts_output, 'w', encoding='utf-8') as f:
        f.write(ts_content)
    
    preserved_count = sum(1 for key in existing_translations if key in [t[0] for t in translations])
    print(f"[OK] TS file generated manually: {ts_output}")
    if preserved_count > 0:
        print(f"[INFO] Preserved {preserved_count} existing translations")

# ------------------------
# Run lupdate
# ------------------------
def run_lupdate(temp_cpp, ts_output, lupdate_path="lupdate"):
    """Run lupdate and return True if successful, False if language not recognized"""
    cmd = [lupdate_path, temp_cpp, "-ts", ts_output]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    
    # Check if lupdate warned about unrecognized language
    if "target language is not recognized" in result.stderr or "won't be updated" in result.stderr:
        print(f"[WARNING] lupdate did not recognize the language code. Will use manual generation to preserve translations.")
        return False
    
    print(f"[OK] TS file generated: {ts_output}")
    return True

def post_process_ts_file(ts_path, original_json_path, target_language=None):
    """Post-process TS file to replace temporary filename with original JSON filename and fix language code"""
    json_filename = os.path.basename(original_json_path)
    
    try:
        with open(ts_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the temporary cpp filename with the JSON filename in location elements
        import re
        # Pattern to match location filename attributes
        pattern = r'filename="[^"]*temp\.cpp"'
        replacement = f'filename="{json_filename}"'
        content = re.sub(pattern, replacement, content)
        
        # Also replace any full temp paths
        pattern2 = r'filename="[^"]*[/\\][^/\\]*temp\.cpp"'
        content = re.sub(pattern2, replacement, content)
        
        # Fix language code format: use hyphen instead of underscore, and don't add region if not needed
        if target_language:
            # Extract the base filename to get the intended language code
            # The target_language parameter should be the actual language we want (e.g., "en", "pt-BR")
            lang_code_to_use = target_language
        else:
            # Try to extract from filename
            match = re.search(r'_([a-z]{2}(?:-[A-Z0-9]{2,})?)\.ts$', os.path.basename(ts_path))
            if match:
                lang_code_to_use = match.group(1)
            else:
                lang_code_to_use = None
        
        if lang_code_to_use:
            # Replace language attribute in TS file
            # lupdate converts "en" to "en_US" and "pt-BR" to "pt_BR", we want to fix this
            pattern_lang = r'<TS version="[^"]*" language="[^"]*">'
            replacement_lang = f'<TS version="2.1" language="{lang_code_to_use}">'
            content = re.sub(pattern_lang, replacement_lang, content)
        
        with open(ts_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"[INFO] Updated TS file to reference {json_filename}")
        if lang_code_to_use:
            print(f"[INFO] Set language code to: {lang_code_to_use}")
    except Exception as e:
        print(f"[WARNING] Could not post-process TS file: {e}")

# ------------------------
# TS -> JSON
# ------------------------
def set_value_by_path(data, path, value):
    parts = re.split(r'\.(?![^\[]*\])', path)
    current = data
    for i, part in enumerate(parts):
        list_match = re.match(r'(.+)\[(\d+)\]$', part)
        if list_match:
            key, idx = list_match.groups()
            idx = int(idx)
            if key not in current:
                current[key] = []
            while len(current[key]) <= idx:
                current[key].append(None)
            if i == len(parts) - 1:
                current[key][idx] = value
            else:
                if current[key][idx] is None:
                    current[key][idx] = {}
                current = current[key][idx]
        else:
            if i == len(parts) - 1:
                current[part] = value
            else:
                if part not in current:
                    current[part] = {}
                current = current[part]

def ts_to_json(ts_path, json_output):
    """Convert TS file back to JSON format"""
    tree = ET.parse(ts_path)
    root = tree.getroot()
    result = {}

    processed_count = 0
    for context in root.findall("context"):
        for message in context.findall("message"):
            # Try to get the JSON path from extracomment
            extracomment_elem = message.find("extracomment")
            source_elem = message.find("source")
            translation_elem = message.find("translation")

            if extracomment_elem is None or source_elem is None:
                continue

            # Get the translation or fall back to source text
            translation_text = ""
            if (translation_elem is not None and 
                translation_elem.text and 
                translation_elem.get("type") != "unfinished"):
                translation_text = translation_elem.text
            else:
                translation_text = source_elem.text

            # Unescape XML entities
            if translation_text:
                translation_text = (translation_text.replace('&quot;', '"')
                                                 .replace('&apos;', "'")
                                                 .replace('&lt;', '<')
                                                 .replace('&gt;', '>')
                                                 .replace('&amp;', '&'))

            # Handle multiple keys in extracomment (when lupdate merges duplicate strings)
            # Split by newlines first, then by spaces, and filter out separator lines like "----------"
            raw_text = extracomment_elem.text
            # First split by newlines
            lines = raw_text.split('\n')
            json_keys = []
            for line in lines:
                line = line.strip()
                # Skip empty lines and separator lines
                if not line or line.startswith('-'):
                    continue
                # Split by spaces to handle cases like "15_ArrowText_0 15_ArrowText_1"
                parts = line.split()
                json_keys.extend(parts)
            
            # Set the value for each key
            for json_key in json_keys:
                if json_key:  # Extra safety check
                    set_value_by_path(result, json_key, translation_text)
                    processed_count += 1

    with open(json_output, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"[OK] JSON file reconstructed: {json_output}")
    print(f"[INFO] Processed {processed_count} translation entries")

# ------------------------
# Main CLI
# ------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert between JSON and TS translation files for TutorialMaker",
        epilog="""
Examples:
  # Convert JSON to TS (English)
  python update_translations.py json2ts text_dict_default.json
  
  # Convert JSON to TS with specific language
  python update_translations.py json2ts text_dict_default_es-ES.json
  
  # Generate multiple language files at once
  python update_translations.py json2ts text_dict_default.json --languages pt-BR,es-419,fr-FR --name monai
  
  # Convert TS back to JSON
  python update_translations.py ts2json text_dict_default_pt-BR.ts
  
  # Specify custom output file
  python update_translations.py json2ts input.json --output custom_output.ts
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("mode", choices=["json2ts", "ts2json"], 
                        help="Conversion mode: json2ts (JSON to TS) or ts2json (TS to JSON)")
    parser.add_argument("input", help="Input file (JSON or TS)")
    parser.add_argument("--output", help="Output file (TS or JSON). If not specified, will be auto-generated based on input filename")
    parser.add_argument("--lupdate", help="Path to lupdate executable (only for json2ts)", 
                        default=r"D:\ArquivosProgramas\Slicer 5.8.1\bin\lupdate.exe")
    parser.add_argument("--context", help="Translation context name (default: TutorialMaker)", default="TutorialMaker")
    parser.add_argument("--languages", help="List of languages to generate TS files for (e.g., pt-BR,es-419,fr-FR)", type=str)
    parser.add_argument("--name", help="Base name for output files when using --languages (e.g., 'monai' generates monai_pt-BR.ts)")
    parser.add_argument("--output-dir", help="Directory where TS files should be generated (default: same as input file)")
    args = parser.parse_args()

    # Validate arguments for multiple languages
    if (args.languages and not args.name) or (args.name and not args.languages):
        parser.error("--languages and --name must be used together")
    
    if args.languages and args.mode != "json2ts":
        parser.error("--languages can only be used with json2ts mode")

    input_dir = os.path.dirname(os.path.abspath(args.input))
    input_base = os.path.basename(args.input)
    context, lang = parse_filename_language(args.input)

    if args.mode == "json2ts":
        # Check if we need to generate multiple language files
        if args.languages and args.name:
            # Parse the languages list
            languages = [lang.strip() for lang in args.languages.split(',')]
            print(f"Generating TS files for languages: {', '.join(languages)}")
            
            # Determine output directory
            output_dir = args.output_dir if args.output_dir else input_dir
            output_dir = os.path.abspath(output_dir)
            
            temp_cpp = json_to_temp_cpp(args.input)
            
            for target_lang in languages:
                # Generate output filename for each language
                output_filename = f"{args.name}_{target_lang}.ts"
                output_path = os.path.join(output_dir, output_filename)
                
                print(f"\n--- Generating {output_filename} ---")
                
                try:
                    lupdate_success = run_lupdate(temp_cpp, output_path, args.lupdate)
                    
                    if lupdate_success:
                        # Post-process the TS file to replace temp filename with JSON filename
                        post_process_ts_file(output_path, args.input, target_lang)
                    else:
                        # lupdate didn't recognize the language, use manual generation
                        print(f"Using manual TS generation to preserve existing translations...")
                        create_ts_manually(temp_cpp, output_path, target_lang, args.context, args.input)
                except FileNotFoundError:
                    print(f"Warning: {args.lupdate} not found. Using manual TS generation as fallback.")
                    create_ts_manually(temp_cpp, output_path, target_lang, args.context, args.input)
                except Exception as e:
                    print(f"Error running lupdate: {e}")
                    print(f"Using manual TS generation as fallback.")
                    create_ts_manually(temp_cpp, output_path, target_lang, args.context, args.input)
            
            os.remove(temp_cpp)
            print(f"\n[SUCCESS] Generated {len(languages)} TS files!")
            
        else:
            # Single file generation (original behavior)
            if not args.output:
                base_name = os.path.splitext(input_base)[0]
                output_filename = f"{base_name}_{lang}.ts"
            else:
                output_filename = os.path.basename(args.output)

            args.output = os.path.join(input_dir, output_filename)

            temp_cpp = json_to_temp_cpp(args.input)
            
            try:
                lupdate_success = run_lupdate(temp_cpp, args.output, args.lupdate)
                
                if lupdate_success:
                    # Post-process the TS file to replace temp filename with JSON filename
                    post_process_ts_file(args.output, args.input, lang)
                else:
                    # lupdate didn't recognize the language, use manual generation
                    print(f"Using manual TS generation to preserve existing translations...")
                    create_ts_manually(temp_cpp, args.output, lang, args.context, args.input)
            except FileNotFoundError:
                print(f"Warning: {args.lupdate} not found. Using manual TS generation as fallback.")
                create_ts_manually(temp_cpp, args.output, lang, args.context, args.input)
            except Exception as e:
                print(f"Error running lupdate: {e}")
                print(f"Using manual TS generation as fallback.")
                create_ts_manually(temp_cpp, args.output, lang, args.context, args.input)
                
            os.remove(temp_cpp)

    elif args.mode == "ts2json":
        if not args.output:
            output_filename = f"{lang}_{input_base}"
            output_filename = os.path.splitext(output_filename)[0] + "_translated.json"
        else:
            output_filename = os.path.basename(args.output)

        args.output = os.path.join(input_dir, output_filename)

        ts_to_json(args.input, args.output)
