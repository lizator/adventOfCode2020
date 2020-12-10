n = 101

mapp = {1: 0,
        2: 0,
        3: 1}

ls = [0]

for i in range(n):
    line = int(input())
    ls.append(line)

ls.sort()

for i in range(len(ls) - 1):
    gap = ls[i + 1] - ls[i]
    if gap < 0 or 3 < gap:
        print("err")
    else:
        mapp[gap] += 1

print(mapp[1] * mapp[3])
