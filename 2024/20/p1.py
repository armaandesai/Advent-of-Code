import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

matrix = [list(line.strip()) for line in lines]
walls = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == "S":
            start = (i, j)
        if matrix[i][j] == "E":
            end = (i, j)
        if matrix[i][j] == "#":
            walls.append((i, j))


def can_reach_end(matrix, start, end):
    queue = [start]
    distances = {start: 0}
    while queue:
        x, y = queue.pop(0)
        if (x, y) == end:
            return distances[end]
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]) and matrix[new_x][new_y] != "#":
                new_distance = distances[(x, y)] + 1
                if (new_x, new_y) not in distances or new_distance < distances[(new_x, new_y)]:
                    distances[(new_x, new_y)] = new_distance
                    queue.append((new_x, new_y))
    return None


base = can_reach_end(matrix, start, end)

total = 0
visited = set()
for i in range(len(walls)):
    x, y = walls[i]
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dir in dirs:
        new_x, new_y = x + dir[0], y + dir[1]
        if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]) and (x, y, new_x, new_y) not in visited:
            visited.add((x, y, new_x, new_y))
            prev = matrix[new_x][new_y]
            matrix[x][y] = "."
            matrix[new_x][new_y] = "."
            distance = can_reach_end(matrix, start, end)
            if distance and base - distance >= 100:
                # print(distance)
                total += 1
            matrix[x][y] = "#"
            matrix[new_x][new_y] = prev
print(total)
