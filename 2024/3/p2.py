import os
import re

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

sum = 0
check = True
for line in lines:

    matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line)
    for m in matches:
        if m == "do()":
            check = True
        elif m == "don't()":
            check = False
        elif check:
            substring = m[4:-1]
            sum += int(substring.split(",")[0]) * int(substring.split(",")[1])
print(sum)