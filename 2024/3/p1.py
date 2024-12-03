import os
import re

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

sum = 0
for line in lines:

    matches = re.findall(r"mul\(\d+,\d+\)", line)
    for m in matches:
        substring = m[4:-1]
        sum += int(substring.split(",")[0]) * int(substring.split(",")[1])
print(sum)