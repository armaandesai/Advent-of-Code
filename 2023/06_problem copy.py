with open("06_problem.txt", "r") as file:
    lines = file.readlines()

times = int("".join(lines[0].strip().split()[1:]))
distances = int("".join(lines[1].strip().split()[1:]))
print(times, distances)
sum = 0
for i in range(times + 1):
    if (i * (times - i) > distances):
        sum += 1
"""for time, distance in zip(times, distances):
    count = 0
    for i in range(time + 1):
        if (i * (time - i) > distance):
            count += 1
    sum *= count
print(sum)"""
print(sum)