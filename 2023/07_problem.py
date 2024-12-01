from collections import Counter

def get_hand(hand):
    sum = 0  
    for char in hand:
        sum *= 16
        if char.isdigit():
            sum += int(char)
        elif char == 'T':
            sum += 10
        elif char == 'J':
            sum += 11
        elif char == 'Q':
            sum += 12
        elif char == 'K':
            sum += 13
        elif char == 'A':
            sum += 14
    count = Counter(hand)
    if count.most_common(1)[0][1] == 5:
        val = 7
    elif count.most_common(1)[0][1] == 4:
        val = 6
    elif count.most_common(2)[0][1] == 3 and count.most_common(2)[1][1] == 2:
        val = 5
    elif count.most_common(2)[0][1] == 3:
        val = 4
    elif count.most_common(2)[0][1] == 2 and count.most_common(2)[1][1] == 2:
        val = 3
    elif count.most_common(2)[0][1] == 2:
        val = 2
    else:
        val = 1
    return (val, sum)

with open("07_problem.txt", "r") as file:
    lines = file.readlines()

hand_bid = {}

for line in lines:
    hand_bid[line.split()[0]] = int(line.split()[1])

hands = list(hand_bid.keys())
sorted_hands = sorted(hands, key=lambda x: get_hand(x))

sum = 0
for i, hand in enumerate(sorted_hands):
    sum += hand_bid[hand] * (i + 1)
print(sum)