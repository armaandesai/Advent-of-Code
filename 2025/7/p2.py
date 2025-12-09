import os
from collections import defaultdict

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

matrix = [list(line.strip()) for line in lines]
splitters = defaultdict(list)
beams = defaultdict(int)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == "S":
            beams[j] = 1
        elif matrix[i][j] == "^":
            splitters[i].append(j)
            
for i in range(len(matrix)):
    new_beams = defaultdict(int)
    for position, count in beams.items():
        if i in splitters and position in splitters[i]:
            new_beams[position - 1] += count
            new_beams[position + 1] += count
        else:
            new_beams[position] += count
    
    beams = new_beams

res = sum(beams.values())
print(res)