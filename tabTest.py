def exportFiles(fileName):
	filePath = "C:\SVNs\Art\Models\Terrain\PrisonDungeon\Door"
	newfilePath = filePath + "\\" + fileName
	mc.file(newfilePath, open = True, f = True)
	armourGrp = mc.ls('armour_*', tr = True)
	skinnedGrp = mc.ls('skinned_*', tr = True)
	tileGrp = mc.ls('tile_*', tr = True)

	if armourGrp:

		mc.select(armourGrp)
		mel.eval("GGG -exportSelected false")
		exportanimSets()

	elif skinnedGrp:

		mc.select(skinnedGrp)
		mel.eval("GGG -exportSelected false")

	elif tileGrp:

		mc.select(tileGrp)
		mel.eval("GGG -exportSelected false")

def exporttileFiles():

	filePath = "C:\SVNs\Art\Models\Terrain\PrisonDungeon\Door"
	# passing argument in batch mode
	dirList = os.listdir(filePath)
	for i in dirList:

		if i.endswith('.mb'):

			exportFiles(i)

		elif i.endswith('china.mb'):

			pass

		else:

			filePath = filePath + "\\" + i
			subdirList = os.listdir(filePath)

			for j in subdirList:

				if i.endswith('.mb'):

				exportFiles(j)

	mc.file(save = True, f = True)
