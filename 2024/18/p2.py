import os


def can_reach_end(matrix, start, end):
    queue = [start]
    distances = {start: 0}
    while queue:
        x, y = queue.pop(0)
        if (x, y) == end:
            return True
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < size + 1 and 0 <= new_y < size + 1 and matrix[new_x][new_y] == ".":
                new_distance = distances[(x, y)] + 1
                if (new_x, new_y) not in distances or new_distance < distances[(new_x, new_y)]:
                    distances[(new_x, new_y)] = new_distance
                    queue.append((new_x, new_y))
    return False


current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()


def create_matrix(n):
    matrix = [list("." * (size + 1)) for _ in range(size + 1)]
    for i, line in enumerate(lines[:n]):
        y, x = list(map(int, line.strip().split(",")))
        matrix[x][y] = "#"
    return matrix


size = 70
start = (0, 0)
end = (size, size)

low, high = 0, 3000
result = float("inf")
while low <= high:
    mid = (low + high) // 2
    matrix = create_matrix(mid)
    if can_reach_end(matrix, start, end):
        low = mid + 1
    else:
        result = min(result, mid)
        high = mid - 1

print(result)
print(lines[result - 1])
