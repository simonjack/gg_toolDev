import maya.cmds as mc
import os
import maya.mel as mel


class skinnedToarmour():

    def __init__(self):
        self.animFileName = "\\animExport"
        # path = self.path

    def loadJts(self, nameSpaces):

        if nameSpaces is None:

            rootJt = mc.ls(type='joint')
            curves = mc.ls(type='nurbsCurve')
        else:
            pass

        babies = rootJt + curves

        return babies
        # babiesLoad = mc.select(babies)

    def loadCurves(self, nameSpaces):

        if nameSpaces is None:
            ctrls = mc.select('ctrl_*')
        else:
            ctrls = mc.select(nameSpaces + 'ctrl_*')

        ctrlsSel = mc.ls(selection=True)
        curveList = []

        for curves in ctrlsSel:
            if mc.nodeType(curves) == 'nurbsCurve':
                curveList.append(curves)

        return curveList

    def exportAnimCurves(self):
        animPath = os.path.split(mc.file(q=True, sn=True))[0]

        snSel = []
        babies = self.loadJts(None)

        for baby in babies:
            mc.select(baby, add=True)

        mc.file(animPath + self.animFileName, es=True, type='animExport')

        return babies

    def deleteAnimCurves(self):
        newjt = []
        jt_anim = self.loadJts(None)
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

            mc.rename(i, newName)

    def saveFileasRig(self):
        global rigFile

        fp = os.path.split(mc.file(q=True, sn=True))[0]

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
        fileName = os.path.split(self.saveFileasRig()[0])[1]
        origPath = mc.file(q=True, sn=True)

        mc.file(f=True, new=True)
        mc.file(origPath, r=True, iv=True, namespace=str.split(str(fileName), '.')[0])

        mc.select(str.split(str(fileName), '.')[0] + ':root*')
        mc.select(str.split(str(fileName), '.')[0] + ':ctrl_*', add=True)

        nameSpaceSplit = str.split(str(fileName), '.')[0] + ":"

        newBabies = self.loadJts(None)
        print newBabies

        for baby in newBabies:
            mc.select(baby, add=True)

        mc.file(filePathopen + self.animFileName + ".anim", i=True, iv=True, ra=True)

        mc.file(rename=filePathopen + "\\" + newFileName)
        mc.file(save=True, type='mayaBinary')

        return newBabies

    def confirm(self):
        items = self.createFile(None)

        for i in items:
            print "Transferred animations to" + str(i)

    def cleanup(self):

        pathtoClean = os.path.split(mc.file(q=True, sn=True))[0]

        items = os.listdir(pathtoClean)

        for i in items:
            if i.endswith('.anim'):
                os.remove(pathtoClean + "\\" + i)


a = skinnedToarmour()

a.loadJts(None)
a.loadCurves(None)
a.exportAnimCurves()
a.deleteAnimCurves()
a.saveFileasRig()
a.createFile('start once')
a.confirm()
