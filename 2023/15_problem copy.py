with open('15_problem.txt', 'r') as f:
    lines = f.readlines()[0].split(",")

sum = 0
boxes = {k: [] for k in range(256)}

def hash_function(label):
    i = 0
    for char in label:
        i += ord(char)
        i *= 17
        i %= 256
    return i

for line in lines:
    if "=" in line:
        label, value = line.split("=")
        i = hash_function(label)
        if any(label == item[0] for item in boxes[i]):
            for index, (l, v) in enumerate(boxes[i]):
                if l == label:
                    boxes[i][index] = (label, int(value))
                    break
        else:
            boxes[i].append((label, int(value)))
    else:
        label = line.split("-")[0]
        i = hash_function(label)
        if boxes[i] and any(label == item[0] for item in boxes[i]):
            boxes[i] = [item for item in boxes[i] if item[0] != label]
for box in boxes:
    for i, item in enumerate(boxes[box]):
        if item:
            print(box, i, item)
            sum += (box + 1) * (i + 1) * item[1]
print(sum)

