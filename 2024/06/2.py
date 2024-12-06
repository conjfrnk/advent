from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

rows, cols = len(dat), len(dat[0])
lab_map = [list(line) for line in dat]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction_symbols = ["^", ">", "v", "<"]

guard_pos = None
initial_direction = None
for r in range(rows):
    for c in range(cols):
        if lab_map[r][c] in direction_symbols:
            guard_pos = (r, c)
            initial_direction = direction_symbols.index(lab_map[r][c])
            break
    if guard_pos:
        break


def simulate_with_obstacle(grid, obstacle_pos):
    pos = guard_pos
    direction = initial_direction
    visited_states = set()

    while True:
        dr, dc = directions[direction]
        next_r, next_c = pos[0] + dr, pos[1] + dc
        state = (pos[0], pos[1], direction)
        if state in visited_states:
            return True
        visited_states.add(state)
        if next_r < 0 or next_r >= rows or next_c < 0 or next_c >= cols:
            return False
        if grid[next_r][next_c] == "#" or (next_r, next_c) == obstacle_pos:
            direction = (direction + 1) % 4
        else:
            pos = (next_r, next_c)
        if len(visited_states) > rows * cols * 4:
            return True


loop_positions = []
for r in range(rows):
    for c in range(cols):
        if lab_map[r][c] != "." or (r, c) == guard_pos:
            continue
        if simulate_with_obstacle(lab_map, (r, c)):
            loop_positions.append((r, c))

print(len(loop_positions))
