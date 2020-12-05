
mx = 0
for i in range(875):
    line = input()
    res = 0
    for j in range(7):
        if line[j] == 'B':
            res += 2 ** (10 - j)
    if res > mx:
        mx = res

print(mx)
