import math

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

def lcm_multiple(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = lcm(result, numbers[i])
    return result

with open("08_problem.txt", "r") as file:
    lines = file.readlines()

instructions = lines[0].strip()
dict = {}
for line in lines[2:]:
    key = line.split("=")[0].strip()
    value = tuple(line.split("=")[1].strip()[1:-1].split(', '))
    dict[key] = value

values = [value for value in dict.keys() if value.endswith("A")]
nums = []
count = 0
while True:
    for instruction in instructions:
        if instruction == "L":
            values = [dict[value][0] for value in values]
        else:
            values = [dict[value][1] for value in values]
        count += 1
        if values:
            for value in values:
                if value.endswith("Z"):
                    values.remove(value)
                    nums.append(count)
        else:
            break
    if not values:
        break

print(lcm_multiple(nums))
