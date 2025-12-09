import os
from collections import defaultdict

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

matrix = [list(line.strip()) for line in lines]
splitters = defaultdict(list)
beams = None
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == "S":
            beams = {j}
        elif matrix[i][j] == "^":
            splitters[i].append(j)
            
res = 0
for i in range(len(matrix)):
    if i in splitters:
        new_beams = set()
        for splitter in splitters[i]:
            if splitter in beams:
                res += 1
                new_beams.add(splitter - 1)
                new_beams.add(splitter + 1)
                beams.remove(splitter)
        beams = beams | new_beams
print(res)