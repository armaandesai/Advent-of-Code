with open("03_problem.txt", "r") as file:
    lines = file.readlines()

matrix = []
for line in lines:
    matrix.append(["."] + [x for x in line.strip()] + ["."])

matrix.insert(0, ["."] * len(matrix[0]))
matrix.insert(len(matrix), ["."] * len(matrix[0]))

dict = {}
sum = 0
for r in range(len(matrix)):
    num = 0
    adjacent = None
    for c in range(len(matrix[r])):
        if matrix[r][c].isdigit():
            num = num * 10 + int(matrix[r][c])
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if matrix[r + i][c + j] == "*":
                        adjacent = (r + i, c + j)
        elif num != 0:
            if adjacent not in dict:
                dict[adjacent] = [num]
            else:
                dict[adjacent].append(num)
            adjacent = None
            num = 0

for key in dict:
    if len(dict[key]) == 2:
        sum += dict[key][0] * dict[key][1]
print(sum)