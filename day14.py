import sys
sys.setrecursionlimit(100000000)

currMask = ""
mapping = {}


def binarify(nr):
    ret = ""
    for j in range(36):
        curr = 2 ** (35 - j)
        if nr - curr >= 0:
            nr -= curr
            ret += "1"
        else:
            ret += "0"
    return ret



def addRec(pointer, number, insertVal):
    while pointer < len(number):
        if currMask[pointer] == "X":
            tmpLs = list(number)
            tmpLs[pointer] = "1"
            addRec(pointer, "".join(tmpLs), insertVal)
            tmpLs[pointer] = "0"
            addRec(pointer, "".join(tmpLs), insertVal)
        elif currMask[pointer] == "1":
            tmpLs = list(number)
            tmpLs[pointer] = "1"
            number = "".join(tmpLs)
        pointer += 1
    res = 0
    for k in range(len(currMask)):
        res += int(number[k]) * 2 ** (35 - k)
    mapping[res] = insertVal


for i in range(4):#560):
    line = input().split(" = ")
    if line[0] == "mask":
        currMask = line[1]
    else:
        pos = int(line[0][4:-1])
        val = int(line[1])
        binPos = binarify(pos)
        addRec(0, binPos, val)


fin = 0
for key in mapping.keys():
    fin += mapping[key]

print(fin)
