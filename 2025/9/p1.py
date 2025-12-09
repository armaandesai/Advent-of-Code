import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

points = [tuple(map(int, line.strip().split(','))) for line in lines]

res = -1
for i in range(len(points)):
    x1, y1 = points[i]
    for j in range(i + 1, len(points)):
        x2, y2 = points[j]
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        res = max(res, area)
print(res)