import slicer

extensionsManager = slicer.app.extensionsManagerModel()
extensionsManager.downloadAndInstallExtensionByName("LanguagePacks")
extensionsManager.downloadAndInstallExtensionByName("MONAIAuto3DSeg")
extensionsManager.downloadAndInstallExtensionByName("TutorialMaker")
exit()