import os

# Get the directory where this file is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Loop through folders labeled 1-25
for i in range(1, 26):
    folder_path = os.path.join(base_dir, str(i))
    
    # Define the content to be written in p1.py and p2.py
    content = """import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()
"""

    # Write the content to p1.py
    p1_path = os.path.join(folder_path, "p1.py")
    with open(p1_path, "w") as p1_file:
        p1_file.write(content)
    
    # Write the content to p2.py
    p2_path = os.path.join(folder_path, "p2.py")
    with open(p2_path, "w") as p2_file:
        p2_file.write(content)