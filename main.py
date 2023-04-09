import scenes
import stat

# Declare some VARIABLES baby!
global job = 0
global flowers_smelled = False

##############################################################################

job = scenes.intro()

# Intro, cliffside.
flowers_smelled = scenes.cliffside(job)