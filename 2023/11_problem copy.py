with open("11_problem.txt") as f:
    lines = [list(line.strip()) for line in f]

rows = len(lines)
cols = len(lines[0])

emptyRows = []
emptyCols = []

for i, row in enumerate(lines):
    if all(item == "." for item in row):
        emptyRows.append(i)

for j in range(cols):
    column = [lines[i][j] for i in range(rows)]
    if all(item == "." for item in column):
        emptyCols.append(j)

print(emptyRows)
print(emptyCols)

for line in lines:
    print("".join(line))

galaxies = []

for i, line in enumerate(lines):
    for j, item in enumerate(line):
        if item == "#":
            galaxies.append((i, j))

sum = 0
while galaxies:
    galaxy = galaxies.pop()
    for g in galaxies:
        print(galaxy, g)
        x1, x2 = min(galaxy[0], g[0]), max(galaxy[0], g[0])
        y1, y2 = min(galaxy[1], g[1]), max(galaxy[1], g[1])
        xCount = len([num for num in emptyRows if x1 < num < x2])
        yCount = len([num for num in emptyCols if y1 < num < y2])
        sum += abs(g[0] - galaxy[0]) + (999999 * xCount) + abs(g[1] - galaxy[1]) + 999999 * yCount
 

    print()
print(sum)


    

    