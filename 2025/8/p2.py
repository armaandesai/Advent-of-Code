import os
import math
import heapq
from heapq import heappush, heappop, heapify
from collections import Counter

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

junctions = {}
junction_list = []
heap = []

for line in lines:
    coords = tuple([int(val) for val in line.strip().split(",")])
    junctions[coords] = None
    junction_list.append(coords)
    
for i in range(len(junction_list)):
    x1, y1, z1 = junction_list[i]
    for j in range(i + 1, len(junction_list)):
        x2, y2, z2 = junction_list[j]
        dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
        heap.append((dist, (x1, y1, z1), (x2, y2, z2)))
        
heapq.heapify(heap)

id = 1
while True:
    dist, junc1, junc2 = heappop(heap)
    if junctions[junc1] is not None and junctions[junc2] is not None and junctions[junc1] == junctions[junc2]:
        continue
    if junctions[junc1] is None and junctions[junc2] is None:
        junctions[junc1] = id
        junctions[junc2] = id
        id += 1
    elif junctions[junc1] is None and junctions[junc2] is not None:
        junctions[junc1] = junctions[junc2]
    elif junctions[junc2] is None and junctions[junc1] is not None:
        junctions[junc2] = junctions[junc1]
    elif junctions[junc1] is not None and junctions[junc2] is not None:
        old_id = junctions[junc2]
        new_id = junctions[junc1]
        for key in junctions:
            if junctions[key] == old_id:
                junctions[key] = new_id
    
    if len(set(junctions.values())) == 1:
        break
        
print(junc1[0] * junc2[0])