import os
from collections import defaultdict

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

mapping = defaultdict(list)
for line in lines:
    key, values = line.strip().split(":")
    for value in values.strip().split(" "):
        mapping[key].append(value)
        
res = 0
queue = ["you"]
while queue:
    current = queue.pop()
    if current == "out":
        res += 1
        continue
    for neighbor in mapping[current]:
        queue.append(neighbor)
print(res)