import os
import re

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
        p = list(map(int, regex))
        # brute force
        minimum = float("inf")
        for i in range(1, 101):
            for j in range(1, 101):
                if i * a[0] + j * b[0] == p[0] and i * a[1] + j * b[1] == p[1]:
                    if i * 3 + j < minimum:
                        minimum = i * 3 + j
        if minimum != float("inf"):
            total += minimum
print(total)
