###WRITE JSON

import maya.cmds as mc
import json
from os.path import expanduser


winID = 'GGG_FX toolkit'


if cmds.window(winID, exists=True):
    cmds.deleteUI(winID)


cmds.window(winID)


cmds.columnLayout()

# Add controls into this Layout
# whatUSay = cmds.textField()
cmds.button(label='Connect 2dPlacementNode', command='printTxtField(whatUSay)', width=200, height=100,
            highlightColor=(0, 1, 0), c=connectMe)
cmds.button(label='Write Object Transform', command='printTxtField(whatUSay)', width=200, height=100, c= writeObjectPosition)
cmds.button(label='Read Object Transform', command='printTxtField(whatUSay)', width=200, height=100, c = readObjectPosition)



def writeObjectPosition():
    sel = mc.ls(selection=True)

    for i in sel:
        data = {}
        for attr in mc.listAttr(i, keyable=True, unlocked=True):
            print attr
            value = mc.getAttr(i + "." + attr)
            print value
            data.setdefault(str(attr), value)
            f = open(expanduser("~") + '/' + i + '.rp', 'w')
            f.write(json.dumps(data))
            f.close()

def readObjectPosition():


    sel = mc.ls(selection=True)
    ch_values = []
    for i in sel:
        print i
        f = open(expanduser("~") + '/' + i + '.rp', 'r')
        data = f.readlines()
        # print data
        f.close()
        j_data = json.loads(data[0])
        print j_data["translateX"]
        for attr in mc.listAttr(i, keyable=True, unlocked=True):
            # print attr
            # print i+"."+j_data[translateX]
            mc.setAttr(i + "." + attr, j_data[attr])


# connect2dPlacement node to fileTexture

# Select the 2dPlacementNode, then select the fileTextures and run this!!!

def connectMe():
    sel = mc.ls(selection=True)
    connexList = []
    connexList = mc.ls(selection=True)
    idx = len(connexList)
    print connexList
    for i in range(idx):
        if i == 0:
            pass
        else:
            mc.connectAttr(connexList[0] + ".mirrorU", connexList[i] + ".mirrorU", f=True)
            mc.connectAttr(connexList[0] + ".mirrorV", connexList[i] + ".mirrorV", f=True)
            mc.connectAttr(connexList[0] + ".stagger", connexList[i] + ".stagger", f=True)
            mc.connectAttr(connexList[0] + ".wrapU", connexList[i] + ".wrapU", f=True)
            mc.connectAttr(connexList[0] + ".wrapV", connexList[i] + ".wrapV", f=True)
            mc.connectAttr(connexList[0] + ".repeatUV", connexList[i] + ".repeatUV", f=True)
            mc.connectAttr(connexList[0] + ".vertexUvOne", connexList[i] + ".vertexUvOne", f=True)
            mc.connectAttr(connexList[0] + ".vertexUvTwo", connexList[i] + ".vertexUvTwo", f=True)
            mc.connectAttr(connexList[0] + ".vertexUvThree", connexList[i] + ".vertexUvThree", f=True)
            mc.connectAttr(connexList[0] + ".vertexCameraOne", connexList[i] + ".vertexCameraOne", f=True)
            mc.connectAttr(connexList[0] + ".noiseUV", connexList[i] + ".noiseUV", f=True)
            mc.connectAttr(connexList[0] + ".offset", connexList[i] + ".offset", f=True)
            mc.connectAttr(connexList[0] + ".outUV", connexList[i] + ".uvCoord", f=True)