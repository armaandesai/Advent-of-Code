with open('18_problem.txt', 'r') as f:
    lines = f.readlines()

x = 0
y = 0
x_min = 0
y_min = 0

coords = []
coords.append([x, y])
for line in lines:
    dir, dist, _ = line.split()
    if dir == "U":
        x -= int(dist)
    elif dir == "D":
        x += int(dist)
    elif dir == "L":
        y -= int(dist)
    elif dir == "R":
        y += int(dist)
    coords.append([x, y])
    x_min = min(x, x_min)
    y_min = min(y, y_min)

x_max = 0
y_max = 0
for coord in coords:
    coord[0] -= x_min
    coord[1] -= y_min
    x_max = max(coord[0], x_max)
    y_max = max(coord[1], y_max)

matrix = [[0 for i in range(y_max + 1)] for j in range(x_max + 1)]

for i in range(len(coords) - 1):
    x1, y1 = coords[i]
    x2, y2 = coords[i + 1]
    if x1 == x2:
        for j in range(min(y1, y2), max(y1, y2) + 1):
            matrix[x1][j] = 1
    elif y1 == y2:
        for j in range(min(x1, x2), max(x1, x2) + 1):
            matrix[j][y1] = 1

for row in matrix:
    row.insert(0, 0)
    print(row)

for i in range(len(matrix)):
    inside = False
    for j in range(len(matrix[0])):
        if matrix[i][j] == 1:
            inside = not inside
        if inside:
            matrix[i][j] = 1
    
print()

for row in matrix:
    print(row)
    
"""for row in matrix:
    print("".join(str(elem) for elem in row))
"""