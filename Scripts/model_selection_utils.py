"""
Utility function for selecting MONAIAuto3DSeg models with automatic fallback.

This module provides a standalone function that can be imported and used
in any Slicer script to robustly select MONAI models.

Usage:
    from model_selection_utils import findModelId, getModelSearchKeywords
    
    modelId = findModelId("prostate-v1.0.1")
    # Returns exact match or latest version fallback
    
    searchKeywords = getModelSearchKeywords(modelId)
    # Returns translated keywords like "Prostate" or "Brain Tumor"
"""

import re


def findModelId(preferredModelId, logic=None):
    """
    Find a model ID with fallback support.
    
    If the exact model ID is not found, searches for the latest version 
    with the same base name.
    
    Args:
        preferredModelId (str): The preferred model ID (e.g., "prostate-v1.0.1")
        logic (MONAIAuto3DSegLogic, optional): Logic instance. If None, creates a new one.
    
    Returns:
        str: The model ID to use (exact match or latest version fallback)
    
    Raises:
        ValueError: If neither exact match nor fallback can be found
    
    Examples:
        >>> # Exact match found
        >>> findModelId("prostate-v1.0.1")
        'prostate-v1.0.1'
        
        >>> # Fallback to newer version
        >>> findModelId("prostate-v1.0.0")
        'prostate-v1.0.1'  # if v1.0.1 is the latest
        
        >>> # Error if no match
        >>> findModelId("nonexistent-v1.0.0")
        ValueError: Model 'nonexistent-v1.0.0' not found and no fallback available
    """
    if logic is None:
        try:
            import MONAIAuto3DSeg
            logic = MONAIAuto3DSeg.MONAIAuto3DSegLogic()
        except ImportError:
            raise ImportError(
                "MONAIAuto3DSeg extension is not installed or not available. "
                "Please install the MONAIAuto3DSeg extension from the Extension Manager."
            )
    
    # First, try to find exact match
    for model in logic.models:
        if model["id"] == preferredModelId:
            print(f"✓ Model found: {preferredModelId}")
            return preferredModelId
    
    # If exact match not found, extract base name and find latest version
    # Example: "prostate-v1.0.1" -> base: "prostate"
    match = re.match(r"^(.+)-v\d+\.\d+\.\d+$", preferredModelId)
    if match:
        baseName = match.group(1)
        print(f"⚠ Exact model '{preferredModelId}' not found.")
        print(f"  Searching for latest '{baseName}' version...")
        
        # Find all models matching the base name
        matchingModels = []
        for model in logic.models:
            if model["id"].startswith(baseName + "-v"):
                if not model.get("deprecated", False):  # Skip deprecated models
                    matchingModels.append(model)
        
        if matchingModels:
            # Models are already sorted by version (first is latest non-deprecated)
            latestModel = matchingModels[0]
            print(f"✓ Using fallback model: {latestModel['id']}")
            print(f"  Title: {latestModel['title']}")
            print(f"  Version: {latestModel['version']}")
            return latestModel["id"]
    
    # If still not found, raise an error with helpful information
    availableIds = [m['id'] for m in logic.models if not m.get("deprecated", False)]
    errorMsg = (
        f"Model '{preferredModelId}' not found and no fallback available.\n"
        f"Available models:\n"
    )
    for modelId in availableIds[:10]:  # Show first 10
        errorMsg += f"  - {modelId}\n"
    if len(availableIds) > 10:
        errorMsg += f"  ... and {len(availableIds) - 10} more\n"
    
    raise ValueError(errorMsg)


def getModelSearchKeywords(modelId, logic=None):
    """
    Get translated search keywords from model title.
    
    Extracts 1-2 key words from the model's translated title to display 
    in search box for visual feedback.
    
    Args:
        modelId (str): The model ID to get keywords for
        logic (MONAIAuto3DSegLogic, optional): Logic instance. If None, creates a new one.
    
    Returns:
        str: 1-2 key words from the translated model title
    
    Examples:
        >>> getModelSearchKeywords("prostate-v1.0.1")
        'Prostate'  # or 'Próstata' in Portuguese
        
        >>> getModelSearchKeywords("brats-gli-v1.0.0")
        'Brain Tumor'  # or 'BRATS GLI'
        
        >>> getModelSearchKeywords("whole-body-3mm-v1.0.0")
        'Whole body'
    """
    if logic is None:
        try:
            import MONAIAuto3DSeg
            logic = MONAIAuto3DSeg.MONAIAuto3DSegLogic()
        except ImportError:
            return ""
    
    try:
        import slicer
        from slicer.i18n import translate
    except ImportError:
        # If not running in Slicer, just return English title words
        translate = lambda category, text: text
    
    # Find the model
    for model in logic.models:
        if model["id"] == modelId:
            # Get translated title
            translatedTitle = translate("Models", model["title"])
            
            # Extract meaningful keywords (skip common words)
            skipWords = ["segmentation", "quick", "-", "ts1", "ts2", "v1", "v2", "the"]
            words = translatedTitle.split()
            keywords = []
            
            for word in words:
                if word.lower() not in skipWords and len(word) > 2:
                    keywords.append(word)
                    if len(keywords) >= 2:  # Get first 2 meaningful words
                        break
            
            # Return keywords
            if keywords:
                return " ".join(keywords)
            else:
                # Fallback to first word of title
                return words[0] if words else ""
    
    return ""


def listAvailableModels(logic=None, showDeprecated=False):
    """
    List all available models with their details.
    
    Args:
        logic (MONAIAuto3DSegLogic, optional): Logic instance. If None, creates a new one.
        showDeprecated (bool): Whether to show deprecated models. Default False.
    
    Returns:
        list: List of model dictionaries with id, title, version, etc.
    
    Example:
        >>> models = listAvailableModels()
        >>> for model in models:
        ...     print(f"{model['id']}: {model['title']}")
    """
    if logic is None:
        import MONAIAuto3DSeg
        logic = MONAIAuto3DSeg.MONAIAuto3DSegLogic()
    
    models = []
    for model in logic.models:
        if not showDeprecated and model.get("deprecated", False):
            continue
        models.append({
            'id': model['id'],
            'title': model['title'],
            'version': model['version'],
            'description': model.get('description', ''),
            'imagingModality': model.get('imagingModality', ''),
            'deprecated': model.get('deprecated', False)
        })
    
    return models


def findModelsByBaseName(baseName, logic=None, includeDeprecated=False):
    """
    Find all models matching a base name (e.g., all "prostate" versions).
    
    Args:
        baseName (str): Base name to search for (e.g., "prostate", "brats-gli")
        logic (MONAIAuto3DSegLogic, optional): Logic instance. If None, creates a new one.
        includeDeprecated (bool): Whether to include deprecated versions. Default False.
    
    Returns:
        list: List of matching model IDs, sorted by version (newest first)
    
    Example:
        >>> findModelsByBaseName("prostate")
        ['prostate-v1.0.1', 'prostate-v1.0.0']
    """
    if logic is None:
        import MONAIAuto3DSeg
        logic = MONAIAuto3DSeg.MONAIAuto3DSegLogic()
    
    matchingModels = []
    for model in logic.models:
        if model["id"].startswith(baseName + "-v"):
            if includeDeprecated or not model.get("deprecated", False):
                matchingModels.append(model["id"])
    
    return matchingModels


def setModelById(modelId, logic=None, useTranslatedKeywords=True):
    """
    Set the current model in the MONAIAuto3DSeg module by ID.
    
    Args:
        modelId (str): The model ID to set (with fallback support via findModelId)
        logic (MONAIAuto3DSegLogic, optional): Logic instance. If None, creates a new one.
        useTranslatedKeywords (bool): Whether to set search box with translated keywords. Default True.
    
    Returns:
        str: The actual model ID that was set (may differ from input if fallback was used)
    
    Example:
        >>> setModelById("prostate-v1.0.1")
        'prostate-v1.0.1'  # or 'prostate-v1.0.2' if fallback was used
        
        >>> setModelById("prostate-v1.0.1", useTranslatedKeywords=False)
        'prostate-v1.0.1'  # search box will be empty
    """
    if logic is None:
        import MONAIAuto3DSeg
        logic = MONAIAuto3DSeg.MONAIAuto3DSegLogic()
    
    # Use findModelId to support fallback
    actualModelId = findModelId(modelId, logic)
    
    # Set the model in parameter node
    parameterNode = logic.getParameterNode()
    parameterNode.SetParameter("Model", actualModelId)
    
    # Set search box with translated keywords or clear it
    try:
        import slicer
        searchBox = slicer.util.findChild(slicer.util.mainWindow(), "modelSearchBox")
        if searchBox:
            if useTranslatedKeywords:
                searchKeywords = getModelSearchKeywords(actualModelId, logic)
                searchBox.setText(searchKeywords)
            else:
                searchBox.setText("")
    except:
        pass  # Not critical if this fails
    
    return actualModelId


# Example usage in a script
if __name__ == "__main__":
    print("=" * 60)
    print("MONAIAuto3DSeg Model Selection Utility")
    print("=" * 60)
    
    try:
        # Example 1: Find specific model with fallback
        print("\nExample 1: Finding prostate model")
        modelId = findModelId("prostate-v1.0.1")
        print(f"Result: {modelId}\n")
        
        # Example 2: List all available models
        print("Example 2: Listing available models")
        models = listAvailableModels()
        print(f"Found {len(models)} available models:")
        for model in models[:5]:  # Show first 5
            print(f"  - {model['id']}: {model['title']}")
        print()
        
        # Example 3: Find all versions of a specific model
        print("Example 3: Finding all BRATS-GLI versions")
        versions = findModelsByBaseName("brats-gli")
        print(f"Found versions: {versions}\n")
        
    except Exception as e:
        print(f"Error: {e}")
