import os
import io


def CreateFileList(filePath):

    path = "C:\\Users\\Jackson\\git_local\\epk"
    fullPath = []
    files = os.listdir(filePath)
    for file in files:
        fullPath.append(str(path) + "\\" + str(file))

    for x in range(0, len(fullPath), 1):
        print fullPath[x]
    return fullPath


CreateFileList('C:\\Users\\Jackson\\git_local\\epk')


def display_resource(self):
    fileList = CreateFileList(self.filePath).fullpath
    print fileList
    for file in self.fullPath:
        print file

        # f = io.open(r'C:\Users\Jackson\git_local\epk\\1h_axe.epk', encoding='UTF-16')
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            else:
                if "ParticleEffect" in line:
                    particlePath = str.split(str(line), "manticore")
                    petName = str(fName) + "_blade.pet"
                    finalName = particlePath[0] + "manticore\\" + petName
                    print finalName
                elif "TrailEffect" in line:
                    trailPath = str.split(str(line), "manticore")
                    trlName = str(fName) + ".trl"
                    finalName = trailPath[0] + "manticore\\" + trlName
                    print finalName


display_resource()
