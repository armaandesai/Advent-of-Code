import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

res = 0
for line in lines:
    bank = [int(x) for x in line.strip()]
    digits = 12
    curr = 0
    i = 0
    while digits > 0:
        max = -1
        idx = -1
        for j in range(i, len(bank) - digits + 1):
            if bank[j] > max:
                max = bank[j]
                idx = j
        curr = curr * 10 + max
        i = idx + 1
        digits -= 1
    res += curr
print(res)