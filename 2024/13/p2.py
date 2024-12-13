import os
import re
import numpy as np

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()
total = 0
for line in lines:
    if line.startswith("Button A"):
        regex = re.findall(r'\+(\d+)', line)
        a = list(map(int, regex))
    elif line.startswith("Button B"):
        regex = re.findall(r'\+(\d+)', line)
        b = list(map(int, regex))
    elif line.startswith("Prize"):
        regex = re.findall(r'\=(\d+)', line)
        p = [int(x) + 10000000000000 for x in regex]
        # Ax = B
        A = np.array([a, b]).T
        B = np.array(p)
        x = np.linalg.solve(A, B)
        # correct for floating point errors
        x = np.round(x, 2)
        if np.all(np.mod(x, 1) == 0):
            total += int(x[0] * 3 + x[1])
print(total)
