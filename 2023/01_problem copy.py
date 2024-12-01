with open("01_problem.txt", "r") as file:
    lines = file.readlines()

sum = 0

digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for line in lines:
    line = line.strip()
    value = 0

    first_number_index = None
    last_number_index = None
    for index, char in enumerate(line):
        if char.isdigit():
            if first_number_index is None:
                first_number_index = index
            last_number_index = index

    min_val = None
    min_index = None
    max_val = None
    max_index = None
    for digit in digits:
        if line.find(digit) != -1:
            if min_index is None or line.find(digit) < min_index:
                min_index = line.find(digit)
                min_val = digits.index(digit)
        if line.rfind(digit) != -1:
            if max_index is None or line.rfind(digit) > max_index:
                max_index = line.rfind(digit)
                max_val = digits.index(digit)
    
    value = 10 * (min_val if (min_index is not None and min_index < first_number_index) else int(line[first_number_index] if first_number_index is not None else min_val))
    value += (max_val if (max_index is not None and max_index > last_number_index) else int(line[last_number_index] if last_number_index is not None else max_val))
    sum += value
    
print(sum)

