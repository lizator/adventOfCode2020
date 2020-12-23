

contains = {}
found = []


def countWithin(color):
    res = 1
    if contains[color][0][1] == "NONE":
        return 1

    for ls in contains[color]:
        res += ls[0] * countWithin(ls[1])

    return res


for i in range(594):
    line = input()
    line = line.split(" bags contain ")
    currColor = line[0]
    if line[1] == "no other bags.":
        contains[currColor] = [[0, "NONE"]]
        pass
    else:
        insideList = line[1].split(", ")
        for bags in insideList:
            insideColor = bags.split(" ")[1] + " " + bags.split(" ")[2]
            count = int(bags.split(" ")[0])
            if currColor in contains.keys():
                contains[currColor].append([count, insideColor])
            else:
                contains[currColor] = [[count, insideColor]]

print(countWithin("shiny gold") - 1)


""" # first star

isContainedBy = {}
res = [-1] # -1 for shiny gold bag not counting

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
"""
