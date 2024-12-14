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

i = 0
while True:
    x_freq = {}
    y_freq = {}
    for k, v in mapping.items():
        x = v[0]
        y = v[1]
        if x not in x_freq:
            x_freq[x] = 1
        else:
            x_freq[x] += 1
        if y not in y_freq:
            y_freq[y] = 1
        else:
            y_freq[y] += 1
    if max(x_freq.values()) >= 25 or max(y_freq.values()) >= 25:
        matrix = [["." for _ in range(101)] for _ in range(103)]
        for k, v in mapping.items():
            x = v[0]
            y = v[1]
            matrix[y][x] = "#"
        for row in matrix:
            print("".join(row))
        print(i)
        break

    for k, v in mapping.items():
        x = v[0]
        y = v[1]
        v_x = v[2]
        v_y = v[3]
        mapping[k] = ((x + v_x) % 101, (y + v_y) % 103, v_x, v_y)
    i += 1

# import os
# import re

# current_dir = os.path.dirname(os.path.abspath(__file__))
# input_file_path = os.path.join(current_dir, "input.txt")

# with open(input_file_path, "r") as file:
#     lines = file.readlines()

# mapping = {}
# for i, line in enumerate(lines):
#     p, v = line.strip().split(" ")
#     x, y = map(int, p[2:].split(","))
#     v_x, v_y = map(int, v[2:].split(","))
#     mapping[i] = (x, y, v_x, v_y)
# i = 0
# maximum = 0
# with open("output.txt", "w") as output_file:
#     while maximum < 2000:
#         visited = set()
#         check = True
#         for k, v in mapping.items():
#             x = v[0]
#             y = v[1]
#             v_x = v[2]
#             v_y = v[3]
#             mapping[k] = ((x + v_x) % 101, (y + v_y) % 103, v_x, v_y)
#             if (x + v_x % 101, y + v_y % 103) in visited:
#                 check = False
#                 break
#             else:
#                 visited.add((x + v_x % 101, y + v_y % 103))
#         if check:
#             if maximum > 1000:
#                 output_file.write(f"Iteration: {i}\n")
#                 matrix = [["." for _ in range(101)] for _ in range(103)]
#                 for k, v in mapping.items():
#                     x = v[0]
#                     y = v[1]
#                     matrix[y][x] = "#"
#                 for row in matrix:
#                     output_file.write("".join(row) + "\n")
#             maximum += 1
#         i += 1
# print("done")
