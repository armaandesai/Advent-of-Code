import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

matrix = [list(line.strip()) for line in lines]
visited = set()
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
x, y = 0, 0
curr = 0

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == "^":
            x, y = i, j
            break
            
while x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]):
    visited.add((x, y))
    dx = dir[curr][0]
    dy = dir[curr][1]
    if (x + dx) < 0 or (x + dx) >= len(matrix) or (y + dy) < 0 or (y + dy) >= len(matrix[0]):
        break
    if matrix[x + dx][y + dy] == "#":
        curr = (curr + 1) % 4
    x += dir[curr][0]
    y += dir[curr][1]

print(len(visited))
