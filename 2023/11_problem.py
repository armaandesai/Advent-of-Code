with open("11_problem.txt") as f:
    lines = [list(line.strip()) for line in f]

rows = len(lines)
cols = len(lines[0])

j = 0
for _ in range(cols):
    if j >= cols:
        break
    column = [lines[i][j] for i in range(rows)]
    if all(item == "." for item in column):
        for i in range(rows):
            lines[i].insert(j + 1, ".")
        cols += 1
        j += 2
    else:
        j += 1
        
new_lines = []
for i, line in enumerate(lines):
    if all(item == "." for item in line):
        new_lines.append(line)
    new_lines.append(line)

lines = new_lines

for line in lines:
    print("".join(line))

galaxies = []

for i, line in enumerate(lines):
    for j, item in enumerate(line):
        if item == "#":
            galaxies.append((i, j))

sum = 0
while galaxies:
    galaxy = galaxies.pop()
    for g in galaxies:
        print(galaxy, g, abs(g[0] - galaxy[0]) + abs(g[1] - galaxy[1]))
        sum += abs(g[0] - galaxy[0]) + abs(g[1] - galaxy[1])
    print()
print(sum)
    

    