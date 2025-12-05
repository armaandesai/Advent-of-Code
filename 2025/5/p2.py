import os
from collections import defaultdict
current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

fresh = []
res = 0
for line in lines:
    line = line.strip()
    if len(line) == 0:
        break
    start, stop = [int(val) for val in line.split("-")]    
    fresh.append([start, stop])
    
fresh.sort(key=lambda x: x[0])
output = []
cur_start, cur_stop = fresh[0]
for i in range(1, len(fresh)):
    start, stop = fresh[i]
    if start <= cur_stop:
        cur_stop = max(cur_stop, stop)
    else:
        output.append([cur_start, cur_stop])
        cur_start, cur_stop = start, stop   

output.append([cur_start, cur_stop])

res = 0
for start, stop in output:
    res += stop - start + 1

print(res)