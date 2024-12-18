import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

matrix = [list("." * 71) for _ in range(71)]

for i, line in enumerate(lines):
    if i == 1024:
        break
    y, x = list(map(int, line.strip().split(",")))
    matrix[x][y] = "#"

start = (0, 0)
end = (70, 70)

queue = [start]
distances = {start: 0}
while queue:
    x, y = queue.pop(0)
    if (x, y) == end:
        break
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 71 and 0 <= new_y < 71 and matrix[new_x][new_y] == ".":
            new_distance = distances[(x, y)] + 1
            if (new_x, new_y) not in distances or new_distance < distances[(new_x, new_y)]:
                distances[(new_x, new_y)] = new_distance
                queue.append((new_x, new_y))

print(distances[end])
