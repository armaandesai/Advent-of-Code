import os
from collections import deque
from functools import lru_cache

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

matrix = [list(line.strip()) for line in lines]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "S":
            start = (i, j)
        if matrix[i][j] == "E":
            end = (i, j)

minimum = float("inf")
dirs = {1: (0, 1), 2: (1, 0), 3: (0, -1), 4: (-1, 0)}
visited = set()


def bfs(start):
    global minimum
    queue = deque([(start[0], start[1], 0, 1)])
    visited.add((start[0], start[1], 1))

    while queue:
        x, y, score, direction = queue.popleft()
        if (x, y) == end:
            minimum = min(minimum, score)
            continue

        for i in range(1, 5):
            dx, dy = dirs[i]
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]) and matrix[new_x][new_y] != "#":
                if i == direction:
                    new_score = score + 1
                else:
                    new_score = score + 1001

                # Only add to the queue if this (new_x, new_y, new_direction) has not been visited
                if (new_x, new_y, i) not in visited:
                    visited.add((new_x, new_y, i))
                    queue.append((new_x, new_y, new_score, i))


@lru_cache(None)
def dfs(x, y, score, direction):
    global minimum
    if (x, y) == end:
        minimum = min(minimum, score)
        return
    if (x, y, direction) in visited:
        return
    visited.add((x, y, direction))
    for i in range(1, 5):
        dx, dy = dirs[i]
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]) and matrix[new_x][new_y] != "#" and (new_x, new_y, i) not in visited:
            if i == direction:
                dfs(new_x, new_y, score + 1, i)
            else:
                dfs(new_x, new_y, score + 1001, i)
    visited.remove((x, y, direction))


bfs(start)
# dfs(start[0], start[1], 0, 1)
print(minimum)
