
res = 0
count = 0
mapping = {}

for i in range(2212):
    line = input()
    if line == "":
        for key in mapping.keys():
            if mapping[key] == count:
                res += 1
        mapping.clear()
        count = 0
    else:
        count += 1
        for c in line:
            if c in mapping.keys():
                mapping[c] += 1
            else:
                mapping[c] = 1


print(res)
