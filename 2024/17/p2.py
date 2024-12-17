import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()
register = []
register.append(int(lines[0].strip().split(" ")[-1]))
register.append(int(lines[1].strip().split(" ")[-1]))
register.append(int(lines[2].strip().split(" ")[-1]))
cmds = list(map(int, lines[4].strip().split(" ")[-1].split(",")))
output = ""
i = 0
while i < len(cmds):
    opcode, val = cmds[i], cmds[i + 1]
    combo = val if val < 4 else register[val - 4]

    match opcode:
        case 0:
            register[0] //= (2 ** combo)
        case 1:
            register[1] = register[1] ^ val
        case 2:
            register[1] = combo % 8
        case 3:
            if register[0] != 0:
                i = val
                continue
        case 4:
            register[1] = register[1] ^ register[2]
        case 5:
            output += f"{combo % 8},"
        case 6:
            register[1] = register[0] // (2 ** combo)
        case 7:
            register[2] = register[0] // (2 ** combo)
    i += 2
print(output.rstrip(","))
