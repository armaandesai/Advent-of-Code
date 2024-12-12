import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

def dfs(i, j, val):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[i]) or matrix[i][j] != val:
        return 1, 0
    if (i, j) in visited:
        return 0, 0
    visited.add((i, j))
    area = 1
    perimeter = 0
    for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        p, a = dfs(x, y, val)
        perimeter += p
        area += a
    return perimeter, area

matrix = [list(line.strip()) for line in lines]
visited = set()
total = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if (i, j) not in visited:
            perimeter, area = dfs(i, j, matrix[i][j])
            total += area * perimeter

print(total)
