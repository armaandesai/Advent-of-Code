with open('15_problem.txt', 'r') as f:
    lines = f.readlines()[0].split(",")

sum = 0
for line in lines:
    val = 0
    for char in line:
        val += ord(char)
        val *= 17
        val = val % 256
    sum += val

print(sum)