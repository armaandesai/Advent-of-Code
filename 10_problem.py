with open("10_problem.txt") as f:
    lines = [list(line.strip()) for line in f]

def print_lines():
    for line in lines:
        res = "".join([str(elem) for elem in line])

        print(res)

def new_dfs(prev, symbol, i, j):
    if i < 0 or i >= len(lines) or j < 0 or j >= len(lines[0]) or lines[i][j] not in ["-", "|", "L", "J", "F", "Y"]:
        return
    print(prev, symbol, ":", i, j, lines[i][j])

    before = lines[i][j]
    if symbol == "S":
        if i > prev[0] and lines[i][j] in ["|", "L", "J"]:
            lines[i][j] = 1 + int(lines[prev[0]][prev[1]])
            new_dfs((i, j), before, i + 1, j)
            new_dfs((i, j), before, i - 1, j)
            new_dfs((i, j), before, i, j + 1)
            new_dfs((i, j), before, i, j - 1)
        elif i < prev[0] and lines[i][j] in ["|", "Y", "F"]:
            lines[i][j] = 1 + int(lines[prev[0]][prev[1]])
            new_dfs((i, j), before, i + 1, j)
            new_dfs((i, j), before, i - 1, j)
            new_dfs((i, j), before, i, j + 1)
            new_dfs((i, j), before, i, j - 1)
        elif j > prev[1] and lines[i][j] in ["-", "J", "Y"]:
            lines[i][j] = 1 + int(lines[prev[0]][prev[1]])
            new_dfs((i, j), before, i + 1, j)
            new_dfs((i, j), before, i - 1, j)
            new_dfs((i, j), before, i, j + 1)
            new_dfs((i, j), before, i, j - 1)
        elif j < prev[1] and lines[i][j] in ["-", "L", "F"]:
            lines[i][j] = 1 + int(lines[prev[0]][prev[1]])
            new_dfs((i, j), before, i + 1, j)
            new_dfs((i, j), before, i - 1, j)
            new_dfs((i, j), before, i, j + 1)
            new_dfs((i, j), before, i, j - 1)
    if symbol == "-":
        if j > prev[1] and lines[i][j] in ["-", "J", "Y"]:
            lines[i][j] = 1 + int(lines[prev[0]][prev[1]])
            new_dfs((i, j), before, i + 1, j)
            new_dfs((i, j), before, i - 1, j)
            new_dfs((i, j), before, i, j + 1)
            new_dfs((i, j), before, i, j - 1)
        elif j < prev[1] and lines[i][j] in ["-", "L", "F"]:
            lines[i][j] = 1 + int(lines[prev[0]][prev[1]])
            new_dfs((i, j), before, i + 1, j)
            new_dfs((i, j), before, i - 1, j)
            new_dfs((i, j), before, i, j + 1)
            new_dfs((i, j), before, i, j - 1)
    if symbol == "|":
        if i > prev[0] and lines[i][j] in ["|", "L", "J"]:
            lines[i][j] = 1 + int(lines[prev[0]][prev[1]])
            new_dfs((i, j), before, i + 1, j)
            new_dfs((i, j), before, i - 1, j)
            new_dfs((i, j), before, i, j + 1)
            new_dfs((i, j), before, i, j - 1)
        elif i < prev[0] and lines[i][j] in ["|", "Y", "F"]:
            lines[i][j] = 1 + int(lines[prev[0]][prev[1]])
            new_dfs((i, j), before, i + 1, j)
            new_dfs((i, j), before, i - 1, j)
            new_dfs((i, j), before, i, j + 1)
            new_dfs((i, j), before, i, j - 1)
    if symbol == "L":
        if i < prev[0] and lines[i][j] in ["|", "Y", "F"]:
            lines[i][j] = 1 + int(lines[prev[0]][prev[1]])
            new_dfs((i, j), before, i + 1, j)
            new_dfs((i, j), before, i - 1, j)
            new_dfs((i, j), before, i, j + 1)
            new_dfs((i, j), before, i, j - 1)
        elif j > prev[1] and lines[i][j] in ["-", "J", "Y"]:
            lines[i][j] = 1 + int(lines[prev[0]][prev[1]])
            new_dfs((i, j), before, i + 1, j)
            new_dfs((i, j), before, i - 1, j)
            new_dfs((i, j), before, i, j + 1)
            new_dfs((i, j), before, i, j - 1)
    if symbol == "J":
        if i < prev[0] and lines[i][j] in ["|", "Y", "F"]:
            lines[i][j] = 1 + int(lines[prev[0]][prev[1]])
            new_dfs((i, j), before, i + 1, j)
            new_dfs((i, j), before, i - 1, j)
            new_dfs((i, j), before, i, j + 1)
            new_dfs((i, j), before, i, j - 1)
        elif j < prev[1] and lines[i][j] in ["-", "L", "F"]:
            lines[i][j] = 1 + int(lines[prev[0]][prev[1]])
            new_dfs((i, j), before, i + 1, j)
            new_dfs((i, j), before, i - 1, j)
            new_dfs((i, j), before, i, j + 1)
            new_dfs((i, j), before, i, j - 1)
    if symbol == "F":
        if i > prev[0] and lines[i][j] in ["|", "L", "J"]:
            lines[i][j] = 1 + int(lines[prev[0]][prev[1]])
            new_dfs((i, j), before, i + 1, j)
            new_dfs((i, j), before, i - 1, j)
            new_dfs((i, j), before, i, j + 1)
            new_dfs((i, j), before, i, j - 1)
        elif j > prev[1] and lines[i][j] in ["-", "J", "Y"]:
            lines[i][j] = 1 + int(lines[prev[0]][prev[1]])
            new_dfs((i, j), before, i + 1, j)
            new_dfs((i, j), before, i - 1, j)
            new_dfs((i, j), before, i, j + 1)
            new_dfs((i, j), before, i, j - 1)
    if symbol == "Y":
        if i > prev[0] and lines[i][j] in ["|", "L", "J"]:
            lines[i][j] = 1 + int(lines[prev[0]][prev[1]])
            new_dfs((i, j), before, i + 1, j)
            new_dfs((i, j), before, i - 1, j)
            new_dfs((i, j), before, i, j + 1)
            new_dfs((i, j), before, i, j - 1)
        elif j < prev[1] and lines[i][j] in ["-", "L", "F"]:
            lines[i][j] = 1 + int(lines[prev[0]][prev[1]])
            new_dfs((i, j), before, i + 1, j)
            new_dfs((i, j), before, i - 1, j)
            new_dfs((i, j), before, i, j + 1)
            new_dfs((i, j), before, i, j - 1)




start = None
visited = []
for i in range(len(lines)):
    row = []
    for j in range(len(lines[0])):
        if lines[i][j] == "S":
            lines[i][j] = 0
            start = (i, j)
            row.append(0)
        else:
            row.append(-1)
        if lines[i][j] == "7":
            lines[i][j] = "Y"
    visited.append(row)


print(start)

new_dfs(start, "S", start[0] + 1, start[1])
new_dfs(start, "S", start[0] - 1, start[1])
new_dfs(start, "S", start[0], start[1] + 1)
new_dfs(start, "S", start[0], start[1] - 1)

max = 1
for line in lines:
    for char in line:
        if isinstance(char, int) and char > max:
            max = char

print_lines()

print(max // 2 + 1)
            
