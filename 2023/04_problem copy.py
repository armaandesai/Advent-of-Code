import re

with open("04_problem.txt", "r") as file:
    lines = file.readlines()

sum = 0
for i, line in enumerate(lines):
    count = 0
    chunks = re.split(r"[:|]", line)
    winning = chunks[1].strip().split(" ")
    selections = chunks[2].strip().split(" ")
    for selection in selections:
        if selection and selection in winning:
            count += 1
    val = 2 ** (count - 1) if count > 0 else 0
print(sum)