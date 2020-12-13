
def rotate(point):
    x = point[0]
    y = point[1]
    newY = -1 * x
    newX = y
    return [newX, newY]


        #   x   y
waypoint = [10, 1]


x = 0
y = 0
for i in range(755):
    line = input()

    if line[0] == "F":
        x += int(line[1:]) * waypoint[0]
        y += int(line[1:]) * waypoint[1]

    if line[0] == "E":
        waypoint[0] += int(line[1:])
    elif line[0] == "W":
        waypoint[0] -= int(line[1:])
    elif line[0] == "N":
        waypoint[1] += int(line[1:])
    elif line[0] == "S":
        waypoint[1] -= int(line[1:])
    elif line[0] == "R":
        rot = int(int(line[1:]) / 90)
        for j in range(rot):
            waypoint = rotate(waypoint)
    elif line[0] == "L":
        rot = int(int(line[1:]) / 90)
        for j in range(4 - rot):
            waypoint = rotate(waypoint)


print(abs(x) + abs(y))