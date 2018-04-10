import maya.cmds as mc
import maya.mel as mel
#mc.loadPlugin("animImportExport.mll")
from os.path import expanduser

selection = mc.ls(selection = True)
homeDir = expanduser("~")

frameStart = 0
frameEnd = 100

for objs in selection:
    path = homeDir + objs + ".anim"
    mel.eval("file - force - options;intValue=17;
                          nodeNames=0;"
                          verboseUnits=0;"
                          whichRange=2;range=frameStart:frameEnd;options=curve;hierarchy=none;controlPoints=0;shapes=1;helpPictures=0;useChannelBox=0;copyKeyCmd=-animation objects -time >0:10> -float >0:10> -option curve -hierarchy none -controlPoints 0 -shape 1 " - typ
    "animExport" - pr - es" + path)
    "C:/tmp/pSphere1.anim";

