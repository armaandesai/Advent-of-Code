import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

towels = []
patterns = lines[0].strip().split(", ")
for line in lines[2:]:
    towels.append(line.strip())

cache = {}


def algo2(towel, cache):
    # print(towel)
    if len(towel) == 0:
        return True
    if towel in cache:
        return cache[towel]
    for pattern in patterns:
        if towel.startswith(pattern):
            if algo(towel[len(pattern):], cache):
                cache[towel] = True
                return True
    return False


def algo(towel):
    n = len(towel)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for pattern in patterns:
            pattern_len = len(pattern)
            if i >= pattern_len and dp[i - pattern_len] and towel[i - pattern_len:i] == pattern:
                dp[i] = True
                break

    return dp[n]


total = 0
for i, towel in enumerate(towels):
    print(i)
    if (algo(towel)):
        total += 1

print(total)
