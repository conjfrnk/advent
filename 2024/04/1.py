from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

grid = [list(line.strip()) for line in dat if line.strip()]

word = "XMAS"
word_length = len(word)

count = 0

rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == word[0]:
            for dx, dy in directions:
                x, y = i, j
                match = True
                for k in range(1, word_length):
                    x += dx
                    y += dy
                    if x < 0 or x >= rows or y < 0 or y >= cols:
                        match = False
                        break
                    if grid[x][y] != word[k]:
                        match = False
                        break
                if match:
                    count += 1

print(count)
