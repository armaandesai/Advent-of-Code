import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

l1 = []
l2 = {}
sum = 0
for line in lines:
    v1, v2 = line.split("   ")
    l1.append(int(v1))
    if int(v2) in l2:
        l2[int(v2)] += 1
    else:
        l2[int(v2)] = 1

for v1 in l1:
    if v1 in l2:
        sum += v1 * l2[v1]

print(sum)