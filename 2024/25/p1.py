import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

matrix = []
locks = []
keys = []
for line in lines:
    line = line.strip()
    if len(line) == 0:
        # do calculation
        counts = [-1] * len(matrix[0])
        for col in range(len(matrix[0])):
            for row in range(len(matrix)):
                if matrix[row][col] == "#":
                    counts[col] += 1
        if matrix[0][0] == "#":
            locks.append(counts)
        else:
            keys.append(counts)
        matrix = []
    else:
        matrix.append(list(line))

counts = [-1] * len(matrix[0])
for col in range(len(matrix[0])):
    for row in range(len(matrix)):
        if matrix[row][col] == "#":
            counts[col] += 1
if matrix[0][0] == "#":
    locks.append(counts)
else:
    keys.append(counts)

total = 0
for lock in locks:
    for key in keys:
        check = True
        for x, y in zip(lock, key):
            if x + y > 5:
                check = False
                break
        if check:
            total += 1

print(total)
