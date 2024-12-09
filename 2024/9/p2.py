import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

input = lines[0].strip()
files = []
empty = []
id = 0
for i, c in enumerate(input):
    if i % 2 == 0:
        for j in range(int(c)):
            files.append(str(id))
        id += 1
    else:
        for j in range(int(c)):
            empty.append(len(files))
            files.append(None)

for empty_space in empty:
    if empty_space > len(files):
        break
    files[empty_space] = files.pop()
    while files[-1] == None:
        files.pop()

total = 0
for i, f in enumerate(files):
    total += i * int(f)
print(total)