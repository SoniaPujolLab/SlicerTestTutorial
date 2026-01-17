#!/usr/bin/env python3
"""
Script to setup tutorial files in TutorialMaker extension directory
This needs to run BEFORE executing the tutorial tests
"""

import sys
import os
import json
import shutil
from pathlib import Path
import glob

def find_tutorialmaker_dir():
    """Find TutorialMaker extension directory"""
    
    # Most common location for installed extensions
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
    Setup tutorial annotation and translation files in TutorialMaker directory
    
    Args:
        tutorial_name: Full tutorial name (e.g., STC-GEN-101_WelcomeTutorial)
        tutorial_dir: Path to tutorial directory in repository
        languages: List of language codes
    """
    print(f"\n=== Setting up files for: {tutorial_name} ===")
    
    # Find TutorialMaker directory
    tutorialmaker_dir = find_tutorialmaker_dir()
    
    # Create Outputs/Annotations directory
    annotations_dir = tutorialmaker_dir / "Outputs" / "Annotations"
    annotations_dir.mkdir(parents=True, exist_ok=True)
    print(f"Annotations directory: {annotations_dir}")
    
    # Extract tutorial name without ID
    tutorial_name_only = tutorial_name
    if '_' in tutorial_name_only:
        tutorial_name_only = tutorial_name_only.split('_', 1)[1]
    
    print(f"Tutorial name (without ID): {tutorial_name_only}")
    
    # Copy tutorial JSON file as annotations.json
    translations_dir = Path(tutorial_dir) / "Translations"
    
    # Try multiple naming patterns
    json_candidates = [
        translations_dir / f"{tutorial_name}.json",  # Full name
        translations_dir / f"{tutorial_name_only}.json",  # Name without ID
    ]
    
    annotations_json = annotations_dir / "annotations.json"
    copied = False
    
    for candidate in json_candidates:
        if candidate.exists():
            print(f"✅ Copying {candidate} -> {annotations_json}")
            shutil.copy2(candidate, annotations_json)
            copied = True
            break
    
    if not copied:
        print(f"⚠️  Warning: Tutorial JSON not found. Tried:")
        for candidate in json_candidates:
            print(f"  - {candidate}")
    
    # Copy translation files
    print(f"\nCopying translation files for languages: {languages}")
    for language in languages:
        lang_file = translations_dir / f"text_dict_{language}.json"
        target_file = annotations_dir / f"text_dict_{language}.json"
        
        if lang_file.exists():
            print(f"✅ Copying {lang_file.name} -> {target_file}")
            shutil.copy2(lang_file, target_file)
        else:
            print(f"⚠️  Warning: Translation not found: {lang_file}")
            # Create empty fallback
            with open(target_file, 'w', encoding='utf-8') as f:
                json.dump({}, f)
            print(f"   Created empty translation file")
    
    # List final state
    print(f"\nFinal annotations directory contents:")
    for file in sorted(annotations_dir.glob("*.json")):
        size = file.stat().st_size
        print(f"  - {file.name} ({size} bytes)")
    
    print("\n✅ Tutorial files setup completed!")

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
