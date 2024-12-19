from collections import deque
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "21_problem.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

matrix = [list(line.strip()) for line in lines]


def bfs(i, j, count):
    q = deque([(i, j, count)])
    while q:
        current_level = []
        for _ in range(len(q)):
            current_level.append(q.popleft())
        step = current_level[0][2]
        if step == 64:
            return len(current_level)
        visited = set()
        for i, j, count in current_level:
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] != "#" and (x, y) not in visited:
                    q.append((x, y, count + 1))
                    visited.add((x, y))
    return 0


for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == "S":
            print(bfs(i, j, 0))
