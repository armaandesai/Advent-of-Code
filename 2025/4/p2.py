import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()
    
# counts adjacent "@"
def check(i, j):
    count = 0
    x = [-1, 0, 1]
    y = [-1, 0, 1]
    for a in x:
        for b in y:
            if 0 <= i + a < len(matrix) and 0 <= j + b < len(matrix[i]):
                if matrix[i + a][j + b] == "@":
                    count += 1
    return count

res = 0
matrix = [list(line.strip()) for line in lines]
while True:
    change = False
    visited = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == ".":
                continue
            if(check(i, j) < 5): #5 because including itself
                change = True
                visited.add((i, j))
                res += 1
    for x, y in visited:
        matrix[x][y] = "."
    if not change:
        break
    
print(res)  