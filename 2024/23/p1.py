import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

adj = {}
for line in lines:
    x, y = line.strip().split("-")
    if x not in adj:
        adj[x] = []
    adj[x].append(y)
    if y not in adj:
        adj[y] = []
    adj[y].append(x)

unique = set()
for i in adj:
    for j in adj:
        for k in adj:
            if i != j and j != k and k != i and i.startswith("t") or j.startswith("t") or k.startswith("t"):
                if j in adj[i] and k in adj[j] and i in adj[k]:
                    unique.add(tuple(sorted([i, j, k])))

print(len(unique))
