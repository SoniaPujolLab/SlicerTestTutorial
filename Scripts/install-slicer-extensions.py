import slicer
import time
import os

def log_message(msg):
    print(f"[Extension Install] {msg}")

log_message("Starting extension installation...")

# Get extensions manager
extensionsManager = slicer.app.extensionsManagerModel()

# Show extension paths
extensions_path = extensionsManager.extensionsInstallPath()
log_message(f"Extensions install path: {extensions_path}")

# Make sure the directory exists
if not os.path.exists(extensions_path):
    log_message(f"Creating extensions directory: {extensions_path}")
    os.makedirs(extensions_path, exist_ok=True)

# List of extensions to install
extensions_to_install = ["LanguagePacks", "MONAIAuto3DSeg", "TutorialMaker"]

# Install each extension
for ext_name in extensions_to_install:
    log_message(f"Installing extension: {ext_name}")
    
    # Check if already installed
    if extensionsManager.isExtensionInstalled(ext_name):
        log_message(f"  -> {ext_name} already installed")
        continue
    
    # Download and install
    extensionsManager.downloadAndInstallExtensionByName(ext_name)
    
    # Wait for installation to complete (check periodically)
    max_wait = 60  # 60 seconds timeout
    wait_interval = 2
    elapsed = 0
    
    while elapsed < max_wait:
        slicer.app.processEvents()
        time.sleep(wait_interval)
        elapsed += wait_interval
        
        if extensionsManager.isExtensionInstalled(ext_name):
            log_message(f"  -> {ext_name} installed successfully!")
            break
        
        if elapsed % 10 == 0:
            log_message(f"  -> Waiting for {ext_name}... ({elapsed}s)")
    
    if not extensionsManager.isExtensionInstalled(ext_name):
        log_message(f"  -> WARNING: {ext_name} installation timeout or failed")

# Final verification
log_message("\n=== Installation Summary ===")
installed_extensions = extensionsManager.installedExtensions
log_message(f"Total installed extensions: {len(installed_extensions)}")
for ext in installed_extensions:
    log_message(f"  - {ext}")

# List extension directories
log_message(f"\nChecking extension directories in: {extensions_path}")
if os.path.exists(extensions_path):
    subdirs = [d for d in os.listdir(extensions_path) if os.path.isdir(os.path.join(extensions_path, d))]
    log_message(f"Found {len(subdirs)} directories:")
    for subdir in subdirs[:10]:  # Show first 10
        log_message(f"  - {subdir}")

log_message("\nExtension installation script completed")

# Give time for everything to finalize
log_message("Waiting for finalization...")
for i in range(3):
    slicer.app.processEvents()
    time.sleep(1)

exit()