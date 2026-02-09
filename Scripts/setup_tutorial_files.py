#!/usr/bin/env python3
"""Setup tutorial files in TutorialMaker extension directory"""

import sys
import os
import json
import shutil
from pathlib import Path
import glob

def find_tutorialmaker_dir():
    """Find TutorialMaker extension directory"""
    
    patterns = [
        "/opt/slicer/slicer.org/Extensions-*/TutorialMaker/lib/Slicer-*/qt-scripted-modules",
        "/opt/slicer/lib/Slicer-*/qt-scripted-modules/TutorialMaker",
        "/opt/slicer/lib/Slicer-*/extensions-*/TutorialMaker*",
    ]
    
    for pattern in patterns:
        matches = glob.glob(pattern)
        if matches:
            path = Path(matches[0])
            print(f"✅ Found TutorialMaker at: {path}")
            return path
    
    print("❌ ERROR: TutorialMaker extension not found!")
    print("Searched patterns:")
    for pattern in patterns:
        print(f"  - {pattern}")
    sys.exit(1)

def setup_tutorial_files(tutorial_name, tutorial_dir, languages):
    """
    Setup tutorial files in TutorialMaker directory
    
    Args:
        tutorial_name: Full tutorial name (e.g., STC-GEN-101_WelcomeTutorial)
        tutorial_dir: Path to tutorial directory in repository
        languages: List of language codes
    """
    print(f"\n=== Setting up files for: {tutorial_name} ===")
    
    tutorialmaker_dir = find_tutorialmaker_dir()
    
    # Create annotations directory for THIS specific tutorial
    tutorial_name_only = tutorial_name.split('_', 1)[1] if '_' in tutorial_name else tutorial_name
    print(f"Tutorial name (without ID): {tutorial_name_only}")
    
    annotations_dir = tutorialmaker_dir / "Outputs" / "Annotations" / tutorial_name_only
    annotations_dir.mkdir(parents=True, exist_ok=True)
    
    testing_dir = tutorialmaker_dir / "Testing"
    testing_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy tutorial Python file to Testing directory
    tutorial_py = Path(tutorial_dir) / f"{tutorial_name_only}.py"
    if tutorial_py.exists():
        target_py = testing_dir / f"{tutorial_name_only}.py"
        print(f"✅ Copying {tutorial_py.name} -> {target_py}")
        shutil.copy2(tutorial_py, target_py)
    else:
        print(f"❌ ERROR: Tutorial Python file not found: {tutorial_py}")
        sys.exit(1)
    
    # Copy tutorial JSON file
    translations_dir = Path(tutorial_dir) / "Translations"
    
    json_candidates = [
        translations_dir / f"{tutorial_name}.json",
        translations_dir / f"{tutorial_name_only}.json",
    ]
    
    annotations_json = annotations_dir / "annotations.json"
    copied = False
    
    for candidate in json_candidates:
        if candidate.exists():
            print(f"✅ Copying {candidate.name} -> annotations.json")
            shutil.copy2(candidate, annotations_json)
            copied = True
            break
    
    if not copied:
        print(f"⚠️  Warning: Tutorial JSON not found")
    
    # Copy default text_dict (base translation)
    default_dict = translations_dir / "text_dict_default.json"
    if default_dict.exists():
        target_default = annotations_dir / "text_dict_default.json"
        print(f"✅ Copying text_dict_default.json")
        shutil.copy2(default_dict, target_default)
    
    # Copy translation files
    for language in languages:
        lang_file = translations_dir / f"text_dict_{language}.json"
        target_file = annotations_dir / f"text_dict_{language}.json"
        
        if lang_file.exists():
            print(f"✅ Copying text_dict_{language}.json")
            shutil.copy2(lang_file, target_file)
        else:
            print(f"⚠️  Warning: Translation not found for {language}")
            with open(target_file, 'w', encoding='utf-8') as f:
                json.dump({}, f)
    
    print(f"\n✅ Setup completed for: {tutorial_name_only}")
    print(f"   Annotations directory: {annotations_dir}")
    print(f"   JSON files: {len(list(annotations_dir.glob('*.json')))}")
    print(f"   Python files in Testing: {len(list(testing_dir.glob('*.py')))}")
    
    # List all copied files for verification
    print(f"\nCopied files:")
    for json_file in sorted(annotations_dir.glob('*.json')):
        print(f"   - {json_file.name}")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Setup tutorial files in TutorialMaker')
    parser.add_argument('tutorial_name', help='Tutorial name (e.g., STC-GEN-101_WelcomeTutorial)')
    parser.add_argument('tutorial_dir', help='Path to tutorial directory')
    parser.add_argument('--languages', nargs='+', required=True, help='Language codes')
    
    args = parser.parse_args()
    
    setup_tutorial_files(
        tutorial_name=args.tutorial_name,
        tutorial_dir=args.tutorial_dir,
        languages=args.languages
    )

if __name__ == "__main__":
    main()
