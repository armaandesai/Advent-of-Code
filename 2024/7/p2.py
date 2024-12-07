import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

def func(curr, l, s):
    if not l:
        return curr == s
    new_curr = int(str(curr) + str(l[0]))
    return func(curr + l[0], l[1:], s) or func(curr * l[0], l[1:], s) or func(new_curr, l[1:], s)

total = 0
for line in lines:
    s, l = line.split(":")
    s = int(s)
    l = list(map(int, l.strip().split(" ")))
    if func(l[0], l[1:], s):
        total += s

print(total)