import maya.cmds as mc
import os
import maya.mel as mel
#import maya.standalone
from sys import argv
armourGrp = 0
skinnedGrp = 0


# maya.standalone.initialize()

# mc.loadPlugin("GGGMayaToolUpdaterPlugin2018.mll")


class mayaBatchExporter():

    def __init__(self, filePath):
        global armourGrp, skinnedGrp
        # global skinnedGrp = [];
        self.filePath = filePath

    def fileList(self):
        dirList = os.listdir(self.filePath)

        return dirList

    def exportRig(self):
        files = self.fileList()
        for i in files:
            if i.endswith('rig.mb'):
                fullPath = self.filePath + "\\" + i
                mc.file(fullPath, open=True, f=True)

                armourGrp = mc.ls('armour_*', tr=True)
                skinnedGrp = mc.ls('skinned_*', tr=True)

            if armourGrp:
                mc.select(armourGrp)
                mel.eval('GGG -exportSelected false')
            elif skinnedGrp:
                mc.select(skinnedGrp)
                mel.eval('GGG -exportSelected false')
            else:
                pass
        mc.file(save=True, f=True)


s = mayaBatchExporter("C:\\SVNs\\Art\\Models\\Effects\\charged_attack\\surge")
s.exportRig()
