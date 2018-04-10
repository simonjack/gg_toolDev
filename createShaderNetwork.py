import maya.cmds as mc
import pymel.core as pm
import maya.mel as mel
from pymel.all import *


class createGGGShader():
    def __init__(self, *args):
        sel = mc.ls(selection=True)
        self.sel = sel
        self.colorMap = []
        self.normalMap = []
        self.specularMap = []

    def createFileTexture(fileTextureName, p2dName):
        tex = pm.shadingNode('file', name=fileTextureName, asTexture=True, isColorManaged=True)
        if not pm.objExists(p2dName):
            pm.shadingNode('place2dTexture', name=p2dName, asUtility=True)
        p2d = pm.PyNode(p2dName)
        tex.filterType.set(0)
        pm.connectAttr(p2d.outUV, tex.uvCoord)
        pm.connectAttr(p2d.outUvFilterSize, tex.uvFilterSize)
        pm.connectAttr(p2d.vertexCameraOne, tex.vertexCameraOne)
        pm.connectAttr(p2d.vertexUvOne, tex.vertexUvOne)
        pm.connectAttr(p2d.vertexUvThree, tex.vertexUvThree)
        pm.connectAttr(p2d.vertexUvTwo, tex.vertexUvTwo)
        pm.connectAttr(p2d.coverage, tex.coverage)
        pm.connectAttr(p2d.mirrorU, tex.mirrorU)
        pm.connectAttr(p2d.mirrorV, tex.mirrorV)
        pm.connectAttr(p2d.noiseUV, tex.noiseUV)
        pm.connectAttr(p2d.offset, tex.offset)
        pm.connectAttr(p2d.repeatUV, tex.repeatUV)
        pm.connectAttr(p2d.rotateFrame, tex.rotateFrame)
        pm.connectAttr(p2d.rotateUV, tex.rotateUV)
        pm.connectAttr(p2d.stagger, tex.stagger)
        pm.connectAttr(p2d.translateFrame, tex.translateFrame)
        pm.connectAttr(p2d.wrapU, tex.wrapU)
        pm.connectAttr(p2d.wrapV, tex.wrapV)
        return tex

    def createShaderNetwork(self):
        sel = self.sel

        if sel:

            for i in sel:
                shader = mc.shadingNode('blinn', asShader=True, n=i + "_Shader")
                shaderGrp = mel.eval('createNode shadingEngine -n ' + shader + "_SG")
                mc.connectAttr(shader + ".outColor", shaderGrp + ".surfaceShader")
                cTex = createFileTexture(i + '_Clr', 'p2dOne')
                sTex = createFileTexture(i + '_Spec', 'p2dOne')
                nTex = createFileTexture(i + '_Nrm', 'p2dOne')
                bUtil = mc.shadingNode('bump2d', asUtility=True)

                mc.connectAttr(cTex + ".outColor", shader + ".color")
                mc.connectAttr(sTex + ".outColor", shader + ".specularColor")
                mc.connectAttr(nTex + ".outAlpha", bUtil + ".bumpValue")
                mc.connectAttr(bUtil + ".outNormal", shader + ".normalCamera")
                mc.setAttr(bUtil + ".bumpInterp", 1)
        else:
            print "no Object Selected"
        return shader, cTex, sTex, nTex

    def populateAttributes(self):

        mc.setAttr(cTex + ".fileTextureName", self.fileItem[0], type="string")
        mc.setAttr(sTex + ".fileTextureName", self.fileItem[1], type="string")
        mc.setAttr(nTex + ".fileTextureName", self.fileItem[2], type="string")

    def assignSelected(self, *args):
        sel = self.sel

        for i in sel:
            mc.hyperShade(assign=shader)

    def UI(self, *args):
        if (mc.window('gggShaderUI', exists=True)):
            mc.deleteUI('gggShaderUI')

        GGGShaderWindow = mc.window('gggShaderUI', title='gggShaderUI')

        mc.rowColumnLayout(numberOfColumns=3)
        mc.text(label="colorMap")
        self.colorMap = mc.textField()
        colorButton = mc.iconTextButton(style='iconOnly', image1="C:\\Users\\Jackson\\git_local\\personal\\openFileDialogIcon.png", c=Callback(self.openFiledialog, "colorMap"))

        mc.text(label="specularMap")
        self.specularMap = mc.textField()
        specButton = mc.iconTextButton(style='iconOnly', image1="C:\\Users\\Jackson\\git_local\\personal\\openFileDialogIcon.png", c=Callback(self.openFiledialog, "specularMap"))

        mc.text(label="normalMap")
        self.normalMap = mc.textField()
        normButton = mc.iconTextButton(style='iconOnly', image1="C:\\Users\\Jackson\\git_local\\personal\\openFileDialogIcon.png", c=Callback(self.openFiledialog, "normalMap"))

        mc.setParent("..")

        mc.rowColumnLayout(numberOfColumns=1)

        mc.button(label="makeNetwork", c=self.main)

        mc.showWindow(GGGShaderWindow)

        return colorButton, specButton, normButton

    def openFiledialog(self, arg1, *args):
        fileItem = mc.fileDialog2(startingDirectory="C:\\SVNs\\Art\\Particles\\", fileFilter="imageFiles (*.png)", fileMode=1)

        map = "self.colorMap"
        print map

        mc.textField(self.colorMap, edit=True, tx=fileItem[0])

        return fileItem

    def main(self):
        createShaderNetwork()
        populateAttributes()
        assignSelected()


a = createGGGShader()
a.UI()
