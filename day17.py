

def addEmptySurround(ls):
    ltom = []
    planetom = []
    for i in range(len(ls[0][0]) + 2):
        ltom.append(0)

    for i in range(len(ls[0]) + 2):
        planetom.append(ltom)

    for i in range(len(ls)):
        for j in range(len(ls[i])):
            ls[i][j].insert(0, 0)
            ls[i][j].append(0)
        ls[i].insert(0, ltom)
        ls[i].append(ltom)

    ls.insert(0, planetom)
    ls.append(planetom)


def findNabos(x, y, z, ls):
    nabos = 0
    if ls[z][y][x] == 1:
        nabos = -1
    for i in range(3):
        currz = z - 1 + i
        for j in range(3):
            curry = y - 1 + j
            for k in range(3):
                currx = x - 1 + k
                nabos += ls[currz][curry][currx]
    return nabos


def calcState(x, y, z, ls):
    if ls[z][y][x] == 1:
        nabos = findNabos(x, y, z, ls)  # -1 for counting self
        if 2 <= nabos <= 3:
            return 1
        return 0
    else:
        nabos = findNabos(x, y, z, ls)
        if nabos == 3:
            return 1
        return 0


mainL = [[]]
line = input()
while line != "":
    currLine = []
    for c in line:
        if c == ".":
            currLine.append(0)
        else:
            currLine.append(1)
    mainL[0].append(currLine)
    line = input()

addEmptySurround(mainL)

for l in range(2):
    addEmptySurround(mainL)
    print(mainL)
    for z in range(len(mainL) - 2):
        myZ = z + 1

        for y in range(len(mainL[0]) - 2):
            myY = y + 1
            for x in range(len(mainL[0][0]) - 2):
                myX = x + 1
                mainL[myZ][myY][myX] = calcState(myX, myY, myZ, mainL)
    print(l)
    for z in range(len(mainL) - 2):
        print(mainL[z+1])




