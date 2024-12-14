import os
import re

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

mapping = {}
for i, line in enumerate(lines):
    p, v = line.strip().split(" ")
    x, y = map(int, p[2:].split(","))
    v_x, v_y = map(int, v[2:].split(","))
    mapping[i] = (x, y, v_x, v_y)

for i in range(100):
    for k, v in mapping.items():
        x = v[0]
        y = v[1]
        v_x = v[2]
        v_y = v[3]
        mapping[k] = ((x + v_x) % 101, (y + v_y) % 103, v_x, v_y)

q1, q2, q3, q4 = 0, 0, 0, 0
for k, v in mapping.items():
    if v[0] == 101 // 2 or v[1] == 103 // 2:
        continue
    if v[0] < 101 // 2 and v[1] < 103 // 2:
        q1 += 1
    elif v[0] < 101 // 2 and v[1] > 103 // 2:
        q2 += 1
    elif v[0] > 101 // 2 and v[1] < 103 // 2:
        q3 += 1
    else:
        q4 += 1

print(q1 * q2 * q3 * q4)
