import maya.cmds as mc
def getVtxPos(shapeNode):
    vtxWorldPosition = []  # will contain positions un space of all object vertex

    vtxIndexList = cmds.getAttr(shapeNode + ".vrts", multiIndices=True)

    for i in vtxIndexList:
        curPointPosition = cmds.xform(str(shapeNode) + ".pnts[" + str(i) + "]", query=True, translation=True,
                                      worldSpace=True)  # [1.1269192869360154, 4.5408735275268555, 1.3387055339628269]
        vtxWorldPosition.append(curPointPosition)
        print vtxWorldPosition

    return vtxWorldPosition

#mc.select("pCube*")

sel = mc.ls(selection = True)
for i in sel:
    getVtxPos(i)



