import os
import re

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

matrix = []
ops = None
for line in lines:
    line = line.strip()
    line = re.sub(r'\s+', ' ', line)
    line = line.split(" ")
    if line[0].isdigit():
        matrix.append([int(val) for val in line])
    else:
        ops = line
res = 0
for i, op in enumerate(ops):
    if op == '*':
        total = 1
        for j in range(len(matrix)):
            total *= matrix[j][i]
    else:
        total = 0
        for j in range(len(matrix)):
            total += matrix[j][i]
    res += total
print(res)