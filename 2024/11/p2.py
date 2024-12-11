import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

stones = list(map(int, lines[0].strip().split(" ")))
cache = {}

def blink(stone, n):
    if n == 0:
        return 1
    if (stone, n) not in cache:
        if stone == 0:
            result = blink(1, n - 1)
        elif len(str(stone)) % 2 == 0:
            stone = str(stone)
            result = 0
            result += blink(int(stone[:len(stone) // 2]), n - 1)
            result += blink(int(stone[len(stone) // 2:]), n - 1)
        else:
            result = blink(2024 * stone, n - 1)
        cache[(stone, n)] = result
    return cache[(stone, n)]

res = 0
for stone in stones:
    res += blink(stone, 75)
print(res)