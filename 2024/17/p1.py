import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

a = int(lines[0].strip().split(" ")[-1])
b = int(lines[1].strip().split(" ")[-1])
c = int(lines[2].strip().split(" ")[-1])
cmds = list(map(int, lines[4].strip().split(" ")[-1].split(",")))
output = ""
mapping = [0, 1, 2, 3, "A", "B", "C"]

i = 0
while i < len(cmds):
    opcode, val = cmds[i], mapping[cmds[i + 1]]
    print(i, a, b, c)

    if val == "A":
        val = a
    elif val == "B":
        val = b
    elif val == "C":
        val = c

    match opcode:
        case 0:
            a //= (2 ** val)
        case 1:
            b = b ^ val
        case 2:
            b = val % 8
        case 3:
            if a != 0:
                i = val
                continue
        case 4:
            print(b, c, "YAY")
            b = b ^ c
        case 5:
            output += f"{val % 8},"
        case 6:
            b = a // (2 ** val)
        case 7:
            c = a // (2 ** val)
    i += 2
print(output.rstrip(","))
