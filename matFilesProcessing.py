import os
import glob

path = "C:\\SVNs\\Art\\particles\\monster_particles\\nemesis_mods\\fire_mod\\fire_projectile"

file_items = os.listdir(path)
mat_files = []
lines = []

for i in file_items:
    if i.endswith('.material'):
        mat_files.append(i)

    else:
        pass


for i in mat_files:
    with open(i, 'r') as read:
        for line in read:
            lines.append(line)


print lines
