with open("02_problem.txt", "r") as file:
    lines = file.readlines()

sum = 0

for line in lines:
    check = True
    start = line.find("Game ") + len("Game ")
    end = line.find(":", start)
    number = int(line[start:end])
    
    game = line[end + 1:].strip()
    rounds = game.split(";")
    for round in rounds:
        cubes = round.split(",")
        for cube in cubes:
            if ("red" in cube and int(cube.split()[0]) > 12) or ("green" in cube and int(cube.split()[0]) > 13) or ("blue" in cube and int(cube.split()[0]) > 14):
                check = False
                break
        if not check:
            break
    sum += number if check else 0

print(sum)