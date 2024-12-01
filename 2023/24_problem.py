hailstones = []

with open("24_problem.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    hailstones.append(tuple([int(val.strip()) for val in line.strip().replace("@", ",").split(",")]))

for hailstone in hailstones:
    px, py, pz, vx, vy, vz = hailstone
    print(px, py, pz, vx, vy, vz)