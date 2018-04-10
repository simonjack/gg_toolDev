import os
path = "C:\\Users\\Jackson\\git_local\\personal\\fire_mod\\rigPath.path"

data = open(path, "r")
IDx = 0
for line in data:
    if IDx == 0:
        filePath = line
        IDx = IDx + 1
    elif IDx == 1:
        rigPath = line
    else:
        pass

print filePath
