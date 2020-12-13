import copy

sides = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]


def findSeating(currGrid, y, x):
    if (y == 0 and x == 0) or (y == len(currGrid) - 1 and x == 0) or (y == 0 and x == len(currGrid[0]) - 1) or (y == len(currGrid) - 1 and x == len(currGrid[0]) - 1):
        return 3
    res = 0
    sideCounter = -1
    if y == 0:
        sideCounter = 2
    elif x == 0:
        sideCounter = 0
    elif y == len(currGrid) - 1:
        sideCounter = 6
    elif x == len(currGrid[0]) - 1:
        sideCounter = 4

    if sideCounter != -1:
        for j in range(5):
            side = sides[(j + sideCounter) % 8]
            curry = y
            currx = x
            freeView = False
            while currGrid[curry + side[0]][currx + side[1]] == -1:
                curry += side[0]
                currx += side[1]
                if not (0 <= curry + side[0] <= len(currGrid) - 1 and 0 <= currx + side[1] <= len(currGrid[0]) - 1):
                    freeView = True
                    break

            if not freeView:
                res += currGrid[curry + side[0]][currx + side[1]]
        return res

    for j in range(8):
        side = sides[j]
        curry = y
        currx = x
        freeView = False
        while currGrid[curry + side[0]][currx + side[1]] == -1:
            curry += side[0]
            currx += side[1]
            if not (0 < curry < len(currGrid) - 1 and 0 < currx < len(currGrid[0]) - 1):
                freeView = True
                break
        if not freeView:
            res += currGrid[curry + side[0]][currx + side[1]]
    return res


grid = []
for i in range(97):
    line = input()
    gridLine = []
    for c in line:
        if c == "L":
            gridLine.append(1)  # all ready occupied (save 1 iteration)
        else:
            gridLine.append(-1)
    grid.append(gridLine)

oldGrid = []
while True:

    if oldGrid != []:
        changed = False
        for y in range(len(grid)):
            if changed:
                break
            for x in range(len(grid[0])):
                if oldGrid[y][x] != grid[y][x]:
                    changed = True
                    break

        if not changed:
            break
    oldGrid = copy.deepcopy(grid)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if oldGrid[y][x] != -1:
                found = findSeating(oldGrid, y, x)
                if found >= 5:
                    grid[y][x] = 0
                elif found == 0:
                    grid[y][x] = 1

fin = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == 1:
            fin += 1

print(fin)
