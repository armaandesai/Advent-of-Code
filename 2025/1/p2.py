import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

res = 0
num = 50

for line in lines:
    mag = int(line[1:])
    for _ in range(mag):
        if line.startswith('L'):
            if num == 0:
                num = 99
            else:
                num = (num - 1) % 100
        else:
            num = (num + 1) % 100
        if num == 0:
            res += 1
        
print(res)
