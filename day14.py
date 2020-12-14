

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


currMask = ""
mapping = {}

for i in range(560):
    line = input().split(" = ")
    if line[0] == "mask":
        currMask = line[1]
    else:
        pos = int(line[0][4:-1])
        val = int(line[1])
        binVal = binarify(val)
        res = 0
        for k in range(len(currMask)):
            if currMask[k] == "X":
                res += int(binVal[k]) * 2 ** (35 - k)
            else:
                res += int(currMask[k]) * 2 ** (35 - k)
        mapping[pos] = res

fin = 0
for key in mapping.keys():
    fin += mapping[key]

print(fin)
