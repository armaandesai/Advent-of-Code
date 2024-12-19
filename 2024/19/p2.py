import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

towels = []
patterns = lines[0].strip().split(", ")
for line in lines[2:]:
    towels.append(line.strip())


def algo(towel):
    n = len(towel)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for pattern in patterns:
            pattern_len = len(pattern)
            if i >= pattern_len and dp[i - pattern_len] > 0 and towel[i - pattern_len:i] == pattern:
                dp[i] += dp[i - pattern_len]

    return dp[n]


total = 0
for i, towel in enumerate(towels):
    total += algo(towel)

print(total)
