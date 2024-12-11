import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

stones = list(map(int, lines[0].strip().split(" ")))

for i in range(25):
    length = len(stones)
    i = 0
    while i < length:
        if stones[i] == 0:
            stones[i] = 1
        elif len(str(stones[i])) % 2 == 0:
            first = str(stones[i])[:len(str(stones[i])) // 2]
            second = str(stones[i])[len(str(stones[i])) // 2:]
            stones[i] = int(first)
            stones.insert(i + 1, int(second))
            length += 1
            i += 1
        else:
            stones[i] *= 2024
        i += 1

print(len(stones))