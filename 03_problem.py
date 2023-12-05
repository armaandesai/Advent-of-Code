with open("03_problem.txt", "r") as file:
    lines = file.readlines()

matrix = []
for line in lines:
    matrix.append(["."] + [x for x in line.strip()] + ["."])

matrix.insert(0, ["."] * len(matrix[0]))
matrix.insert(len(matrix), ["."] * len(matrix[0]))

sum = 0
for r in range(len(matrix)):
    num = 0
    check = False
    for c in range(len(matrix[r])):
        if matrix[r][c].isdigit():
            num = num * 10 + int(matrix[r][c])
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if matrix[r + i][c + j] != "." and not matrix[r + i][c + j].isdigit():
                        check = True
        elif num != 0:
            if check:
                sum += num
                check = False
            num = 0

print(sum)