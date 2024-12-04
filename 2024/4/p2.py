import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

def find(i, j):
    global total
    if matrix[i - 1][j - 1] == "M" and matrix[i - 1][j + 1] == "M" and matrix[i + 1][j - 1] == "S" and matrix[i + 1][j + 1] == "S":
        total += 1
    elif matrix[i - 1][j - 1] == "M" and matrix[i - 1][j + 1] == "S" and matrix[i + 1][j - 1] == "M" and matrix[i + 1][j + 1] == "S":
        total += 1
    elif matrix[i - 1][j - 1] == "S" and matrix[i - 1][j + 1] == "S" and matrix[i + 1][j - 1] == "M" and matrix[i + 1][j + 1] == "M":
        total += 1
    elif matrix[i - 1][j - 1] == "S" and matrix[i - 1][j + 1] == "M" and matrix[i + 1][j - 1] == "S" and matrix[i + 1][j + 1] == "M":
        total += 1
    

total = 0

matrix = []
for line in lines:
    matrix.append(list(line.strip()))

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "A" and i - 1 >= 0 and i + 1 < len(matrix) and j - 1 >= 0 and j + 1 < len(matrix[i]):
            find(i, j)
            

print(total)