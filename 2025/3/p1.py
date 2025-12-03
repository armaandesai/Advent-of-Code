import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

res = 0
for line in lines:
    bank = [int(x) for x in line.strip()]
    curr = 0
    for i in range(0, len(bank) - 1):
        for j in range(i + 1, len(bank)):
            curr = max(curr, bank[i] * 10 + bank[j])
    res += curr
print(res)