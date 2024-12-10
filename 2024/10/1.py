from pathlib import Path
from collections import deque

# fn = "ex1.txt"
# fn = "ex2.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

grid = [list(line) for line in dat]
rows = len(grid)
cols = len(grid[0])

heights = [[int(c) for c in row] for row in grid]
directions = [(1,0),(-1,0),(0,1),(0,-1)]
trailheads = [(r,c) for r in range(rows) for c in range(cols) if heights[r][c] == 0]

total_score = 0

for start_r, start_c in trailheads:
    if heights[start_r][start_c] != 0:
        continue
    reached_nines = set()
    visited = set()
    queue = deque()
    queue.append((start_r, start_c, 0))
    visited.add((start_r, start_c, 0))
    while queue:
        r, c, h = queue.popleft()
        if h == 9:
            reached_nines.add((r,c))
            continue
        nh = h + 1
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if heights[nr][nc] == nh:
                    state = (nr, nc, nh)
                    if state not in visited:
                        visited.add(state)
                        queue.append(state)
    total_score += len(reached_nines)

print(total_score)
