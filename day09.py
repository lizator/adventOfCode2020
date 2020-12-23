
pre = []
al = []
sz = 25
res = 0


def find(nr):
    for i in range(len(pre)):
        for j in range(len(pre) - i - 1):
            if pre[i] + pre[j + 1 + i] == nr:
                return True
    return False


def cont(target, index):
    point = index
    mx = -1
    mn = -1
    r = 0
    while r < target:
        if mx == -1:
            mx = al[point]
            mn = al[point]
        else:
            if mx < al[point]:
                mx = al[point]
            if mn > al[point]:
                mn = al[point]
        r += al[point]
        point -= 1
    if r == target:
        print("max: " + str(mx))
        print("min: " + str(mn))
        print("sum: " + str(mx + mn))
        return True
    return False


while True:
    if len(pre) < sz:
        line = int(input())
        al.append(line)
        pre.append(line)
    else:
        line = int(input())
        al.append(line)
        if find(line):
            pre.pop(0)
            pre.append(line)
        else:
            res = line
            break

counter = len(al) - 2
while counter != -1 and not cont(res, counter):
    counter -= 1
