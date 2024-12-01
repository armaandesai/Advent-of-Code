with open("06_problem.txt", "r") as file:
    lines = file.readlines()

times = list(map(int, lines[0].strip().split()[1:]))
distances = list(map(int, lines[1].strip().split()[1:]))
sum = 1
for time, distance in zip(times, distances):
    count = 0
    for i in range(time + 1):
        if (i * (time - i) > distance):
            count += 1
    sum *= count
print(sum)