import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

check = True
matrix = []
dirs = ""
for line in lines:
    if len(line.strip()) == 0:
        check = False
    if check:
        matrix.append(list(line.strip()))
    else:
        dirs += line.strip()

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "@":
            curr = (i, j)
            break

mapping = {
    "<": (0, -1),
    ">": (0, 1),
    "^": (-1, 0),
    "v": (1, 0)
}
for dir in dirs:
    x, y = curr
    dx, dy = mapping[dir]
    if matrix[x + dx][y + dy] == "#":
        continue
    elif matrix[x + dx][y + dy] == ".":
        matrix[x + dx][y + dy] = "@"
        matrix[x][y] = "."
        curr = (x + dx, y + dy)
    else:
        i = 1
        while matrix[x + dx * i][y + dy * i] == "O":
            i += 1
        if matrix[x + dx * i][y + dy * i] == "#":
            continue
        matrix[x + dx * i][y + dy * i] = "O"
        matrix[x + dx][y + dy] = "@"
        matrix[x][y] = "."
        curr = (x + dx, y + dy)

total = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == "O":
            total += i * 100 + j
print(total)
