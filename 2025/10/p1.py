import os
from collections import deque

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

def solve_machine(target, buttons):
    n_lights = len(target)
    initial_state = tuple([False] * n_lights)
    target_state = tuple(target)
    
    if initial_state == target_state:
        return 0
    
    queue = deque([(initial_state, 0)])  # (current_state, presses)
    visited = {initial_state}
    
    while queue:
        current_state, presses = queue.popleft()
        
        # Try pressing each button
        for button in buttons:
            # Create new state by toggling lights affected by this button
            new_state = list(current_state)
            for light_idx in button:
                new_state[light_idx] = not new_state[light_idx]
            new_state = tuple(new_state)
            
            if new_state == target_state:
                return presses + 1
            
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, presses + 1))
    
    return -1  # No solution found

total_presses = 0

for line in lines:
    line = line.strip().split(' ')
    target = [True if val == "#" else False for val in line[0][1:-1]]
    buttons = []
    for item in line[1:-1]:
        buttons.append([int(val) for val in item[1:-1].split(',')])
    
    min_presses = solve_machine(target, buttons)
    total_presses += min_presses

print(total_presses)