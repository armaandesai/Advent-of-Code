from collections import deque

with open("21_problem.txt", "r") as f:
    matrix = [list(line.strip()) for line in f]

def mark_diamond(x, y, depth):
    for i in range(-depth, depth + 1):
        for j in range(-depth, depth + 1):
            if abs(i) + abs(j) <= depth and 0 <= x + i < len(matrix) and 0 <= y + j < len(matrix[0]) and matrix[x + i][y + j] != "#":
                if (i + j) % 2 == 0:
                    matrix[x + i][y + j] = "O"

start = None
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "S":
            start = (0, i, j)
            mark_diamond(i, j, 4)

for row in matrix:
    print("".join(row))

"""order = set()
#set = set()
q = deque()
q.append(start)
while q:
    dist, x, y = q.popleft()
    if dist >= 65:
        break
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[nx]) and matrix[nx][ny] != "#" and (dist + 1) < 2:
            #if dist + 1 == 6:
                #set.add((nx, ny))
            matrix[nx][ny] = "O"
            if (dist + 1) not in order:
                print(dist + 1)
                for row in matrix:
                    print("".join(row))
                print()
            order.add(dist + 1)
            q.append((dist + 1, nx, ny))

for row in matrix:
    print("".join(row))
#print(len(set))"""""

    