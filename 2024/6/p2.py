import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

matrix = [list(line.strip()) for line in lines]
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
start_x, start_y = 0, 0

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == "^":
            start_x, start_y = i, j
            break
count = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        prev = matrix[i][j]
        matrix[i][j] = "#"
        x, y = start_x, start_y
        visited = set()
        curr = 0
        

        while x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]):
            if (x, y, curr) in visited:
                count += 1
                break
            visited.add((x, y, curr))
            dx = dir[curr][0]
            dy = dir[curr][1]
            if (x + dx) < 0 or (x + dx) >= len(matrix) or (y + dy) < 0 or (y + dy) >= len(matrix[0]):
                break
            if matrix[x + dx][y + dy] == "#":
                curr = (curr + 1) % 4
            else:
                x += dir[curr][0]
                y += dir[curr][1]
        matrix[i][j] = prev

print(count)