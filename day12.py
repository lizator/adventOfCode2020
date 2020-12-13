

directions = ["E", "S", "W", "N"]
currDir = 0
x = 0
y = 0
for i in range(755):
    line = input()

    if line[0] == "F":
        line = directions[currDir] + line[1:]

    if i == 14:
        print("test")

    if line[0] == "E":
        x += int(line[1:])
    elif line[0] == "W":
        x -= int(line[1:])
    elif line[0] == "N":
        y += int(line[1:])
    elif line[0] == "S":
        y -= int(line[1:])
    elif line[0] == "R":
        rot = int(int(line[1:]) / 90)
        currDir = (currDir + rot) % 4
    elif line[0] == "L":
        rot = int(int(line[1:]) / 90)
        currDir = int(currDir + 4 - rot) % 4


print(abs(x) + abs(y))