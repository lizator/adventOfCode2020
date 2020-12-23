

ls = []

for i in range(875):
    line = input()
    res = ""
    for j in range(10):
        if line[j] == 'B' or line[j] == 'R':
            res += "1"
        else:
            res += "0"
    tmp = int(res, 2)
    ls.append(tmp)

ls.sort()
for i in range(len(ls)):
    if ls[i] == ls[i+1] - 2:
        print(ls[i]+1)
        break

