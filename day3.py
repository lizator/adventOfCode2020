grid = []

for i in range(323):
    line = input()
    insertLine = []
    for c in line:
        if c == '.':
            insertLine.append(0)
        else:
            insertLine.append(1)
    grid.append(insertLine)

results = []
stearing = [[1, 1],
            [3, 1],
            [5, 1],
            [7, 1],
            [1, 2]]

for i in range(5):
    right = stearing[i][0]
    down = stearing[i][1]
    res = 0
    pos = [0, 0] #y, x
    while pos[0] < len(grid):
        if grid[pos[0]][pos[1]] == 1:
            res += 1
        pos[0] += down
        pos[1] = (pos[1] + right) % len(grid[0])
    results.append(res)

out = 1
for r in results:
    out *= r
print(out)