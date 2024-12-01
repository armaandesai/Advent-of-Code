def translate(seeds, values):
    for i, seed in enumerate(seeds):
        for j, value in enumerate(values):
            if seed >= value[1] and seed <= value[1] + value[2] - 1:
                seeds[i] = seed - value[1] + value[0]
                break
    return seeds
                
with open("05_problem.txt", "r") as file:
    lines = file.readlines()

seeds = list(map(int, lines[0].split(":")[1].strip().split()))
new_seeds = []

for i in range(0, len(seeds), 2):
    new_seeds.extend([seeds[i] + j for j in range(seeds[i + 1])])
seeds = new_seeds

values = []
for i, line in enumerate(lines[3:]):
    if ":" in line:
        seeds = translate(seeds, values)
        values = []
    elif line != "\n":
        values.append(list(map(int, line.strip().split())))
seeds = translate(seeds, values)
print(min(seeds))
        

