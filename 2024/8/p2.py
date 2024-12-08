import os
from collections import defaultdict

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

matrix = []
for line in lines:
    matrix.append(list(line.strip()))

r = len(matrix)
c = len(matrix[0])
visited = set()
mapping = defaultdict(list)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] != ".":
            visited.add((i, j))
            mapping[matrix[i][j]].append((i, j))

for k, v in mapping.items():
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            x1, y1 = v[i]
            x2, y2 = v[j]
            x_diff = x2 - x1
            y_diff = y2 - y1
            new_x1 = x1 - x_diff
            new_y1 = y1 - y_diff
            while 0 <= new_x1 < r and 0 <= new_y1 < c:
                visited.add((new_x1, new_y1))
                new_x1 -= x_diff
                new_y1 -= y_diff
            new_x2 = x2 + x_diff
            new_y2 = y2 + y_diff
            while 0 <= new_x2 < r and 0 <= new_y2 < c:
                visited.add((new_x2, new_y2))
                new_x2 += x_diff
                new_y2 += y_diff

print(len(visited))