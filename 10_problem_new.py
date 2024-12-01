from collections import deque

with open("10_problem.txt") as f:
    lines = [list(line.strip()) for line in f]

def dfs(prev_i, prev_j, prev_symbol, i, j):
    pass

start = None
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == "S":
            lines[i][j] = 0
            start = (i, j)

i, j = start[0], start[1]
print(i, j)

q = deque()
q.append(start)

while q:
    i, j = q.popleft()
    symbol = lines[i][j]