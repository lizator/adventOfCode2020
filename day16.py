line = input()
valids = []
depatureRelated = []

while line != "":
    name = line.split(": ")[1].split(" ")
    if name[0] == "departure":
        depatureRelated.append(True)
    else:
        depatureRelated.append(False)

    line = line.split(": ")[1].split(" or ")
    curr = []
    for c in line:
        a = c.split("-")
        curr.append(int(a[0]))
        curr.append(int(a[1]))
    valids.append(curr)
    line = input()

input() #your ticket
myTicket = input().split(",")

input()
input()
near = input()
outerList = []
while near != "":
    valid = True
    near = near.split(",")
    lineBoolList = []
    for nr in near:
        found = False
        curr = int(nr)
        boolListForNr = []
        for ranges in valids:
            if ranges[0] <= curr <= ranges[1] or ranges[2] <= curr <= ranges[3]:
                found = True
                boolListForNr.append(True)
            else:
                boolListForNr.append(False)
        if not found:
            valid = False
            break
        else:
            lineBoolList.append(boolListForNr)
    if valid:
        outerList.append(lineBoolList)

    near = input()

ordering = []
for i in range(len(outerList[0])):
    ordering.append(-1)

for i in range(len(outerList[0])):
    print(ordering)
    possible = outerList[0][i]
    for j in range(len(outerList) - 1):
        k = j + 1
        checkList = outerList[k][i]
        for m in range(len(checkList)):
            if possible[m]:
                possible[m] = checkList[m]

    for n in range(len(possible)):
        if possible[n]:
            ordering[n] = i

print(ordering)



