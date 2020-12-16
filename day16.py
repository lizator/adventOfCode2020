line = input()
valids = []

while line != "":
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

timesPossible = {}
ordering = []
endResult = []
for i in range(len(outerList[0])):
    endResult.append(-1)
    ordering.append([])
    timesPossible[i] = 0

for i in range(len(outerList[0])):
    possible = outerList[0][i]
    for j in range(len(outerList) - 1):
        k = j + 1
        checkList = outerList[k][i]
        for m in range(len(checkList)):
            if possible[m]:
                possible[m] = checkList[m]

    for n in range(len(possible)):
        if possible[n]:
            ordering[n].append(i)
            timesPossible[i] += 1

while len(timesPossible.keys()) > 0:
    for key in timesPossible.keys():
        found = False
        if timesPossible[key] == 1:
            for i in range(len(ordering)):
                if key in ordering[i]:
                    found = True
                    endResult[i] = key
                    for possible in ordering[i]:
                        timesPossible[possible] -= 1
                    timesPossible.pop(key)
                    ordering[i].clear()
        if found:
            break

res = 1
for i in range(6):
    res *= int(myTicket[endResult[i]])

print(res)



