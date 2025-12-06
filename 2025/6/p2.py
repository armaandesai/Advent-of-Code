import os
import re

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()
    
matrix = []
longest = -1
for line in lines:
    line = line.rstrip()
    longest = max(longest, len(line))
    matrix.append(line)
    
for i in range(len(matrix)):
    while len(matrix[i]) < longest:
        matrix[i] += " "

symbol = None
res = 0
numbers = []
for i in range(len(matrix[0])):
    if all(matrix[j][i] == " " for j in range(len(matrix))):
        if symbol == "+":
            res += sum(numbers)
        elif symbol == "*":
            prod = 1
            for n in numbers:
                prod *= n
            res += prod
        numbers = []
        continue
    num = 0
    for j in range(len(matrix) - 1):
        if matrix[j][i] != " ":
            num *= 10
            num += int(matrix[j][i])
    numbers.append(num)
    if matrix[-1][i] != " ":
        symbol = matrix[-1][i]

if symbol == "+":
    res += sum(numbers)
elif symbol == "*":
    prod = 1
    for n in numbers:
        prod *= n
    res += prod
    
print(res)