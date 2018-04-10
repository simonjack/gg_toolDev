import maya.cmds as cmds

def printNewMenuItem( item ):
	print item

window = cmds.window(title = 'GGG_ProjectWindow', widthHeight = (512,128))
cmds.rowColumnLayout(numberOfColumns = 1, rowSpacing = (1,10))
cmds.text(label = 'assetName')
cmds.textField()

cmds.optionMenuGrp( label='Asset Type', changeCommand=printNewMenuItem)
cmds.menuItem( label='Player Skill' )
cmds.menuItem( label='Monster Effects' )
cmds.menuItem( label='Environment Effects' )
cmds.menuItem( label='MicroTransaction' )
cmds.button(label = 'Create asset')
cmds.showWindow( window )