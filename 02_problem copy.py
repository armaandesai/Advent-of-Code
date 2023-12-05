import re

with open("02_problem.txt", "r") as file:
    lines = file.readlines()

sum = 0

for line in lines:
    game = ":".join(line.split(":")[1:])
    rounds = re.split(",|;", game)
    r, g, b = 0, 0, 0
    for round in rounds:
        if "red" in round and int(round.strip().split()[0]) > r:
            r = int(round.strip().split()[0])
        elif "green" in round and int(round.strip().split()[0]) > g:
            g = int(round.strip().split()[0])
        elif "blue" in round and int(round.strip().split()[0]) > b:
            b = int(round.strip().split()[0])
    sum += r * g * b
print(sum)