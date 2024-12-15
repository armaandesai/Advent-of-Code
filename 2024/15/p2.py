import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

check = True
matrix = []
dirs = ""
char = {
    "#": "##",
    ".": "..",
    "O": "[]",
    "@": "@."
}
for line in lines:
    if len(line.strip()) == 0:
        check = False
    if check:
        line = line.strip()
        new_line = ""
        for c in line:
            new_line += char[c]
        matrix.append(list(new_line))
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
    for i in range(len(matrix)):
        print("".join(matrix[i]))
    if matrix[x + dx][y + dy] == "#":
        continue
    elif matrix[x + dx][y + dy] == ".":
        matrix[x + dx][y + dy] = "@"
        matrix[x][y] = "."
        curr = (x + dx, y + dy)
    else:
        if dir in "<>":
            i = 1
            while matrix[x + dx * i][y + dy * i] in "[]":
                i += 1
            if matrix[x + dx * i][y + dy * i] == "#":
                continue
            for k in range(i - 1, 0, -1):
                # print(x + dx * k, y + dy * k, matrix[x + dx * k][y + dy * k])
                # print(x + dx * (k + 1), y + dy * (k + 1),
                #       matrix[x + dx * (k + 1)][y + dy * (k + 1)])
                matrix[x + dx * (k + 1)][y + dy * (k + 1)
                                         ] = matrix[x + dx * k][y + dy * k]
            matrix[x + dx][y + dy] = "@"
            matrix[x][y] = "."
            curr = (x + dx, y + dy)
        else:
            pass

total = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == "[":
            total += i * 100 + j
print(total)
