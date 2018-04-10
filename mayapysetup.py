import os
import maya.standalone
from sys import argv
 
# Start Maya in batch mode
maya.standalone.initialize()
 

import maya.cmds as mc
import maya.mel as mel

mc.loadPlugin("GGGMayaToolUpdaterPlugin2018.mll")

def exportanimSets():
   mel.eval("ggg_exportAnimationSet false")

def exportAllFiles():
	filePath = argv[1]
	filePath = filePath + "\\rig.mb"
	mc.file(filePath, open = True, f = True)

	armourGrp = mc.ls('armour_*', tr = True)
	skinnedGrp = mc.ls('skinned_*', tr = True)

	if armourGrp:
		mc.select(armourGrp)
		mel.eval("GGG -exportSelected false")
	elif skinnedGrp:
		mc.select(skinnedGrp)
		mel.eval("GGG -exportSelected false")
	else:
		pass

	mc.file(save = True, f = True)

if __name__ == "__main__":
	exportAllFiles()
	exportanimSets()
	