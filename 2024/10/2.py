from pathlib import Path
from collections import deque

# fn = "ex1.txt"
# fn = "ex2.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

heights = [list(map(int, list(line))) for line in dat]
rows = len(heights)
cols = len(heights[0])
directions = [(1,0),(-1,0),(0,1),(0,-1)]

dp = [[0]*cols for _ in range(rows)]

for r in range(rows):
    for c in range(cols):
        if heights[r][c] == 9:
            dp[r][c] = 1

for h in range(8,-1,-1):
    for r in range(rows):
        for c in range(cols):
            if heights[r][c] == h:
                total = 0
                for dr,dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] == h+1:
                        total += dp[nr][nc]
                dp[r][c] = total

res = sum(dp[r][c] for r in range(rows) for c in range(cols) if heights[r][c] == 0)
print(res)
