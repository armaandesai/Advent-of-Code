with open("09_problem.txt", "r") as file:
    lines = file.readlines()

sum = 0
for line in lines:
    val = 0
    extrapolate = list(map(int, line.strip().split()))[::-1]
    while any(item != 0 for item in extrapolate):
        val += extrapolate[-1]
        new_list = []
        for i in range(1, len(extrapolate)):
            new_list.append(extrapolate[i] - extrapolate[i - 1])
        extrapolate = new_list
    sum += val

print(sum)