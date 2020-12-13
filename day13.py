import math

timeStamp = int(input())
busLines = input().split(",")
mapping = {}

for ID in busLines:
    if ID != "x":
        curr = int(ID)
        mapping[curr] = int(math.ceil(timeStamp/curr)) * curr

mn = [-1, -1]
#    [id, val]
for key in mapping.keys():
    if mn[0] == -1 or mn[1] > mapping[key]:
        mn = [key, mapping[key]]

print(mn[0] * (mn[1] - timeStamp))
