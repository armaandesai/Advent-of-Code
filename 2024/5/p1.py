import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

sum = 0
next = {}
prev = {}
for line in lines:
    if "|" in line:
        a, b = line.strip().split("|")
        if a not in next:
            next[a] = [b]
        else:
            next[a].append(b)
        if b not in prev:
            prev[b] = [a]
        else:
            prev[b].append(a)
    elif "," in line:
        vals = line.strip().split(",")
        check = True
        seen = set()
        for val in vals:
            for item in seen:
                if val in prev and item not in prev[val]:
                    check = False
                    break
            seen.add(val)
        seen = set()
        for val in reversed(vals):
            for item in seen:
                if val in next and item not in next[val]:
                    check = False
                    break
            seen.add(val)
        
        if check:
            sum += int(vals[len(vals) // 2])

print(sum)
