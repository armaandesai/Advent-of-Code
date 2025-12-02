import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

res = 0    
ids = lines[0].split(",")
for id in ids:
    x, y = id.split("-")
    for i in range(int(x), int(y) + 1):
        s = str(i)
        checked = False
        for j in range(1, len(s) // 2 + 1):
            if len(s) % j != 0:
                continue
            pattern = s[0:j]
            if pattern * (len(s) // j) == s:
                checked = True
                break
        if checked:
            # print(i)
            res += i
print(res)