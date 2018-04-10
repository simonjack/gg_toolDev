import maya.cmds as mc
import os
import maya.mel as mel


class skinnedToarmour():

    def __init__(self):
        self.animFileName = "\\animExport"
        # path = self.path

    def loadJts(self):
        joints = mel.eval('GGG-selectCharacterSkeleton')
        rootJt = mc.select('root*')
        rootjtSel = mc.ls(selection=True)

        babies = mc.listRelatives(rootjtSel[0], ad=True, f=True)

        for baby in babies:
            print baby

        return babies
        # babiesLoad = mc.select(babies)

    def exportAnimCurves(self):
        animPath = os.path.split(mc.file(q=True, sn=True))[0]

        snSel = []

        babies = self.loadJts()
        # print babies

        for baby in babies:
            mc.select(baby, add=True)

        mc.file(animPath + self.animFileName, es=True, type='animExport')

    def deleteAnimCurves(self):
        newjt = []
        jt_anim = self.loadJts()
        for jt in jt_anim:
            # print jt
            newjt.append(str(jt).split('|')[-1])

        animCurve = mc.ls(type='animCurve')

        if animCurve:
            mc.delete(animCurve)
        else:
            print "no animations found"

        skinnedGrp = mc.select("skinned_once*")
        skinnedGrpAct = mc.ls(selection=True)

        for i in skinnedGrpAct:
            newName = str.replace(str(i), "skinned_once", "armour_")
            print newName
            mc.rename(i, newName)

    def saveFileasRig(self):
        global rigFile

        fp = os.path.split(mc.file(q=True, sn=True))[0]

        print fp

        animCurve = mc.ls(type='animCurve')
        print animCurve

        if animCurve:
            print "Rig file cannot have animations"

        else:
            rigFile = mc.file(rn=fp + '\\rig.mb')
            mc.file(save=True, type='mayaBinary')

        return rigFile, fp

    def createFile(self, newFileName):
        global rigPath

        filePathopen = os.path.split(mc.file(q=True, sn=True))[0]
        fileName = os.path.split(mc.file(q=True, sn=True))[1]
        origPath = mc.file(q=True, sn=True)

        mc.file(f=True, new=True)
        mc.file(origPath, r=True, iv=True, namespace=str.split(str(fileName), '.')[0])

        mc.select(str.split(str(fileName), '.')[0] + ':root*')
        importSel = mc.ls(selection=True)

        newBabies = mc.listRelatives(importSel[0], ad=True, f=True)

        for baby in newBabies:
            mc.select(baby, add=True)

        mc.file(filePathopen + self.animFileName + ".anim", i=True, iv=True, ra=True)

        mc.file(rename=filePathopen + "\\" + newFileName)
        mc.file(save=True, type='mayaBinary')

    def cleanup(self):

        pathtoClean = os.path.split(mc.file(q=True, sn=True))[0]

        items = os.listdir(pathtoClean)

        for i in items:
            if i.endswith('.anim'):
                os.remove(pathtoClean + "\\" + i)


a = skinnedToarmour()
a.loadJts()
a.exportAnimCurves()
a.deleteAnimCurves()
a.saveFileasRig()
a.createFile('start once')
a.cleanup()
