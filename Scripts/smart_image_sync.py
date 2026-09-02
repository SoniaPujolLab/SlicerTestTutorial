#!/usr/bin/env python3
"""
smart_image_sync.py
Synchronizes generated tutorial output files with the target repository folder.
Avoids updating image files if visual differences are below a perceptual threshold
(e.g., cursor blinking, sub-pixel text anti-aliasing).
"""

import os
import sys
import shutil
import hashlib
import argparse
from pathlib import Path

# Ensure UTF-8 output even on Windows consoles with limited encodings
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if sys.stderr and hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

try:
    from PIL import Image, ImageChops
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

def file_sha256(filepath):
    """Calculate SHA256 hash of a file."""
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def images_are_visually_identical(source_path, target_path, tolerance=0.001):
    """
    Compare two images using PIL with a pixel tolerance threshold.
    
    Args:
        source_path: Path to newly generated image
        target_path: Path to existing image in repository
        tolerance: Maximum acceptable ratio of different pixels (default 0.001 = 0.1%)
        
    Returns:
        tuple (bool identical, float diff_ratio, str reason)
    """
    if not HAS_PIL:
        # Fallback to byte comparison if PIL is not available
        return (file_sha256(source_path) == file_sha256(target_path), 0.0, "PIL not installed; used hash")

    try:
        with Image.open(source_path) as img_src, Image.open(target_path) as img_tgt:
            if img_src.size != img_tgt.size or img_src.mode != img_tgt.mode:
                return (False, 1.0, f"Size or mode mismatch: {img_src.size}/{img_src.mode} vs {img_tgt.size}/{img_tgt.mode}")

            diff = ImageChops.difference(img_src, img_tgt)
            bbox = diff.getbbox()
            if bbox is None:
                return (True, 0.0, "Exact pixel match")

            # Count non-zero difference pixels
            diff_gray = diff.convert('L')
            hist = diff_gray.histogram()
            diff_pixels = sum(hist[1:])
            total_pixels = img_src.size[0] * img_src.size[1]
            diff_ratio = diff_pixels / float(total_pixels)

            if diff_ratio <= tolerance:
                return (True, diff_ratio, f"Diff ratio {diff_ratio*100:.4f}% <= tolerance {tolerance*100:.2f}% ({diff_pixels}/{total_pixels} px)")
            else:
                return (False, diff_ratio, f"Diff ratio {diff_ratio*100:.4f}% > tolerance {tolerance*100:.2f}% ({diff_pixels}/{total_pixels} px)")
    except Exception as e:
        print(f"  ⚠️ Error comparing images {source_path} and {target_path}: {e}")
        return (False, 1.0, f"Comparison error: {e}")

def text_files_are_identical(source_path, target_path):
    """Compare text files normalizing newlines."""
    try:
        with open(source_path, 'r', encoding='utf-8', errors='replace') as f1, \
             open(target_path, 'r', encoding='utf-8', errors='replace') as f2:
            return f1.read().replace('\r\n', '\n') == f2.read().replace('\r\n', '\n')
    except Exception:
        return file_sha256(source_path) == file_sha256(target_path)

def sync_directories(source_dir, target_dir, tolerance=0.001):
    """
    Sync all files from source_dir to target_dir using smart comparison.
    """
    source = Path(source_dir)
    target = Path(target_dir)

    if not source.exists():
        print(f"❌ Source directory does not exist: {source}")
        return False

    target.mkdir(parents=True, exist_ok=True)

    stats = {"unchanged": 0, "updated": 0, "created": 0}

    for src_file in source.glob('*'):
        if not src_file.is_file():
            continue

        tgt_file = target / src_file.name

        # If target file doesn't exist, simply copy
        if not tgt_file.exists():
            shutil.copy2(src_file, tgt_file)
            print(f"  ➕ Created: {src_file.name}")
            stats["created"] += 1
            continue

        # Target exists, check based on file extension
        ext = src_file.suffix.lower()

        if ext in ['.png', '.jpg', '.jpeg']:
            identical, diff_ratio, reason = images_are_visually_identical(src_file, tgt_file, tolerance=tolerance)
            if identical:
                print(f"  ⏭️ Unchanged (kept): {src_file.name} ({reason})")
                stats["unchanged"] += 1
            else:
                shutil.copy2(src_file, tgt_file)
                print(f"  🔄 Updated: {src_file.name} ({reason})")
                stats["updated"] += 1

        elif ext in ['.html', '.md', '.json', '.txt']:
            if text_files_are_identical(src_file, tgt_file):
                print(f"  ⏭️ Unchanged: {src_file.name}")
                stats["unchanged"] += 1
            else:
                shutil.copy2(src_file, tgt_file)
                print(f"  🔄 Updated: {src_file.name}")
                stats["updated"] += 1
        else:
            # Fallback to byte comparison
            if file_sha256(src_file) == file_sha256(tgt_file):
                print(f"  ⏭️ Unchanged: {src_file.name}")
                stats["unchanged"] += 1
            else:
                shutil.copy2(src_file, tgt_file)
                print(f"  🔄 Updated: {src_file.name}")
                stats["updated"] += 1

    print(f"\nSync summary for {target.name}:")
    print(f"  - Created:   {stats['created']}")
    print(f"  - Updated:   {stats['updated']}")
    print(f"  - Unchanged: {stats['unchanged']}")
    return True

def main():
    parser = argparse.ArgumentParser(description="Smartly sync tutorial output images and files.")
    parser.add_argument("--source", required=True, help="Source directory with newly generated files")
    parser.add_argument("--target", required=True, help="Target directory in repository")
    parser.add_argument("--tolerance", type=float, default=0.001,
                        help="Maximum difference ratio for PNGs to be considered unchanged (default: 0.001 = 0.1%%)")

    args = parser.parse_args()
    success = sync_directories(args.source, args.target, tolerance=args.tolerance)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
