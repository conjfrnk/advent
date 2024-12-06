from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")
from pathlib import Path

rows, cols = len(dat), len(dat[0])
lab_map = [list(line) for line in dat]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction_symbols = ["^", ">", "v", "<"]

guard_pos = None
current_direction = None
for r in range(rows):
    for c in range(cols):
        if lab_map[r][c] in direction_symbols:
            guard_pos = (r, c)
            current_direction = direction_symbols.index(lab_map[r][c])
            break
    if guard_pos:
        break

visited_positions = set([guard_pos])

while True:
    dr, dc = directions[current_direction]
    next_r, next_c = guard_pos[0] + dr, guard_pos[1] + dc

    if next_r < 0 or next_r >= rows or next_c < 0 or next_c >= cols:
        break

    if lab_map[next_r][next_c] == "#":
        current_direction = (current_direction + 1) % 4
    else:
        guard_pos = (next_r, next_c)
        visited_positions.add(guard_pos)

print(len(visited_positions))
