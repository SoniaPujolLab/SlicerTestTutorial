# SlicerTutorialMakerCollection
This repository contains tutorials designed for the Tutorial Maker extension

In the latest version, all tutorials are require to use comments directives.

```
[code before BEGIN will be immediately executed]
# TUTORIALMAKER BEGIN

[this is information to generate the tutorials]
# TUTORIALMAKER INFO TITLE The title of the tutorial
# TUTORIALMAKER INFO AUTHOR The author of the tutorial
# TUTORIALMAKER INFO DATE 01/01/2001
# TUTORIALMAKER INFO DESC A Short Description of the tutorial
[before stating the tutorial, you can specify all the dependencies that are required to run the tutorial
that will block TutorialMaker from continuing the capture before the user has installed the extensions
on the actions environment, that extensions will be installed automatically]
# TUTORIALMAKER INFO DEPENDENCIES MONAIAuto3DSeg

[code before taking a screenshot]
# TUTORIALMAKER SCREENSHOT
[code for the next screenshot]
# TUTORIALMAKER SCREENSHOT

# TUTORIALMAKER END
[Everything after that will be ignored. We have a TODO to run this section of code after the tutorial finishes the capture.]
```

Use the FourMinuteTutorial and AIBasedSedgmentationIn3DSlicer as a base to create a new tutorial.
