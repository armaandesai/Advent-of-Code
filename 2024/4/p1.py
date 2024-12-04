import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

def find(str, i, j, direction):
    if len(str) == 0:
        global total
        total += 1
        return
    x, y = directions[direction]
    if i + x < 0 or i + x >= len(matrix) or j + y < 0 or j + y >= len(matrix[i]) or str[:1] != matrix[i + x][j + y]:
        return
    find(str[1:], i + x, j + y, direction)

total = 0

matrix = []
for line in lines:
    matrix.append(list(line.strip()))

directions = {
    1: [0, 1],
    2: [0, -1],
    3: [1, 0],
    4: [-1, 0],
    5: [1, 1],
    6: [-1, -1],
    7: [1, -1],
    8: [-1, 1]
}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "X":
            for k in range(1, 9):
                find("MAS", i, j, k)
            

print(total)