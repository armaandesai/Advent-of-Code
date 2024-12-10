import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

matrix = [list(map(int, line.strip())) for line in lines]
total = 0
def traverse(i, j, curr, visited):
    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] != curr:
        return
    if matrix[i][j] == 9:
        visited.add((i, j))
        return
    return traverse(i+1, j, curr + 1, visited) or traverse(i-1, j, curr + 1, visited) or traverse(i, j+1, curr + 1, visited) or traverse(i, j-1, curr + 1, visited)
    
for i in range(len(matrix)):
    for j in range(len(matrix[1])):
        if matrix[i][j] == 0:
            visited = set()
            traverse(i, j, 0, visited)
            total += len(visited)
                
print(total)