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
        files.append([str(id), int(c)])
        id += 1
    else:
        empty.append([len(files), int(c)])
        files.append([None, int(c)])

print(files)
print(empty)

# while empty and files:
#     last = files.pop()
#     for e in empty:
#         if e[1] >= 

# total = 0
# for i, f in enumerate(files):
#     total += i * int(f)
# print(total)