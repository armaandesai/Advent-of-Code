import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

dict = {}
gates = []
check = True
for line in lines:
    line = line.strip()
    if line == "":
        check = False
        continue
    if check:
        dict[line.split(": ")[0]] = int(line.split(": ")[1])
    else:
        vals = line.split(" ")
        del vals[3]
        gates.append(vals)


while len(gates) > 0:
    delete = []
    for i, gate in enumerate(gates):
        if gate[0] in dict and gate[2] in dict:
            if gate[1] == "AND":
                dict[gate[3]] = dict[gate[0]] & dict[gate[2]]
            elif gate[1] == "OR":
                dict[gate[3]] = dict[gate[0]] | dict[gate[2]]
            else:
                dict[gate[3]] = dict[gate[0]] ^ dict[gate[2]]
            delete.append(i)
    gates = [gate for i, gate in enumerate(gates) if i not in delete]
