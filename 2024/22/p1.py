import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

vals = [int(line.strip()) for line in lines]
total = 0
for val in vals:
    for i in range(2000):
        res = val * 64
        val = val ^ res
        val %= 16777216

        res = val // 32
        val = val ^ res

        res = val * 2048
        val = val ^ res
        val %= 16777216
    total += val

print(total)
