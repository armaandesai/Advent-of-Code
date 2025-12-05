import os
from collections import defaultdict
current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

sep = False
fresh = defaultdict(list)
res = 0
for line in lines:
    line = line.strip()
    if len(line) == 0:
        sep = True
        continue
    if sep:
        id = int(line)
        check = False
        for k in fresh:
            if id < k:
                continue
            vals = fresh[k]
            for val in vals:
                if id <= val:
                    check = True
        if check:
            res += 1
    else:
        start, stop = [int(val) for val in line.split("-")]
        fresh[start].append(stop)

print(res)