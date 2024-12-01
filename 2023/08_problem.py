with open("08_problem.txt", "r") as file:
    lines = file.readlines()

instructions = lines[0].strip()
dict = {}
for line in lines[2:]:
    key = line.split("=")[0].strip()
    value = tuple(line.split("=")[1].strip()[1:-1].split(', '))
    dict[key] = value

count = 0
value = "AAA"
while True:
    for instruction in instructions:
        if instruction == "L":
            value = dict[value][0]
        else:
            value = dict[value][1]
        count += 1
        if value == "ZZZ":
            print(count)
            break
    if value == "ZZZ":
        break