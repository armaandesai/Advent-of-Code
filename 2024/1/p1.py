import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

l1 = []
l2 = []
sum = 0
for line in lines:
    v1, v2 = line.split("   ")
    l1.append(int(v1))
    l2.append(int(v2))
l1.sort()
l2.sort()

for v1, v2 in zip(l1, l2):
    sum += abs(v1 - v2)

print(sum)
