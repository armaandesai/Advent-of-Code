import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

points = [tuple(map(int, line.strip().split(','))) for line in lines]

res = 0

for x1, y1 in points:
    for x2, y2 in points:
        # Ensure each rectangle is only considered once
        if (x1, y1) > (x2, y2):
            continue

        bx1, bx2 = min(x1, x2), max(x1, x2)
        by1, by2 = min(y1, y2), max(y1, y2)

        # Assume rectangle is valid until an edge crosses its interior
        for i, (lx1, ly1) in enumerate(points):
            lx2, ly2 = points[(i + 1) % len(points)]

            # If the segment's bounding box overlaps the rectangle's interior
            horiz_overlap = max(lx1, lx2) > bx1 and bx2 > min(lx1, lx2)
            vert_overlap = max(ly1, ly2) > by1 and by2 > min(ly1, ly2)

            if horiz_overlap and vert_overlap:
                # Edge passes through the rectangle interior: invalidate it
                break
        else:
            area = (bx2 - bx1 + 1) * (by2 - by1 + 1)
            res = max(res, area)

print(res)

            