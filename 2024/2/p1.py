import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()
count = 0
total = []
for line in lines:
    total.append(list(map(int, line.split())))

for vals in total:
    #check increasing or decreasing
    inc = True
    for i in range(1, len(vals)):
        if vals[i] < vals[i - 1]:
            inc = False
            break
    dec = True
    for i in range(1, len(vals)):
        if vals[i] > vals[i - 1]:
            dec = False
            break
    if not inc and not dec:
        continue
    
    #check if the list is valid
    check = True
    for i in range(1, len(vals)):
        diff = abs(vals[i] - vals[i - 1])
        if diff > 3 or diff < 1:
            check = False
            break
    if check:
        count += 1
print(count)