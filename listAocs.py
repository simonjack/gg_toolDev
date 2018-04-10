import fnmatch
import os
import json
path = "C:\\SVNs\\bin\\Client\\Metadata\\Effects\\"
testPath = "C:\\Users\\Jackson\\Documents\\testData\\"

matches = []
for root, dirnames, filenames in os.walk(testPath):
    for filename in fnmatch.filter(filenames, '*.aoc'):
        matches.append(os.path.join(root, filename))




boneGroups = []
for i in matches:
    aocFile = open(i,'r')
    print aocFile.read()



