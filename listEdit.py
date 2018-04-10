a = ['Animations', 'once.mb', 'loop.mb', 'animations', 'loopnoint.mb']
b = ['channel loopnoint.mb', 'emerge once.mb', 'idle loopnoint.mb', 'rig.mb', 'submerge once.mb', 'armour_body', 'armour body.mb']
c = []
animationList = []
for i in b:
    trig = i.split(" ")

    if len(trig) < 2:
        c.append(i)
    elif trig[1] not in a:
        c.append(i)
    else:
        animationList.append(i)

print animationList
