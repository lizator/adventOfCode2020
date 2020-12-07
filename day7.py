

isContainedBy = {}
found = []
res = [-1]


def dive(color):
    if not color in found:
        res[0] += 1
        found.append(color)
        if color in isContainedBy.keys():
            for c in isContainedBy[color]:
                dive(c)


for i in range(594):
    line = input()
    line = line.split(" bags contain ")
    currColor = line[0]
    insideList = line[1].split(", ")
    for bags in insideList:
        insideColor = bags.split(" ")[1] + " " + bags.split(" ")[2]
        if insideColor in isContainedBy.keys():
            isContainedBy[insideColor].append(currColor)
        else:
            isContainedBy[insideColor] = [currColor]

dive("shiny gold")

print(res[0])