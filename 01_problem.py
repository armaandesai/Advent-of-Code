with open("01_problem.txt", "r") as file:
    lines = file.readlines()

sum = 0


for line in lines:
    digits = ''.join([char for char in line if char.isdigit()])
    val = 10 * int(digits[0]) + int(digits[-1])
    sum += val
    
print(sum)
