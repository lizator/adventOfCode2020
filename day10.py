n = 101

mapp = {0: 1}

ls = [0]

for i in range(n):
    line = int(input())
    ls.append(line)
    mapp[line] = 0

ls.sort()

for i in range(len(ls) - 1):
    curr = ls[i]
    for j in range(min(3, len(ls) - 1 - i)):
        possible = ls[i + 1 + j]
        if curr >= possible - 3:  # able to go to it
            mapp[possible] += mapp[curr]
        else:
            break

print(mapp[ls[len(ls) - 1]])








"""for i in range(len(ls) - 1):
    gap = ls[i + 1] - ls[i]
    if gap < 0 or 3 < gap:
        print("err")
    else:
        mapp[gap] += 1

print(mapp[1] * mapp[3])"""
