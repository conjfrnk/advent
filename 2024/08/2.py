from pathlib import Path
from math import gcd

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(fn)
dat = open(fn).read().strip().split("\n")

rows = len(dat)
cols = len(dat[0]) if rows > 0 else 0

antennas = {}
for y, line in enumerate(dat):
    for x, ch in enumerate(line):
        if ch != ".":
            if ch not in antennas:
                antennas[ch] = []
            antennas[ch].append((x, y))

antinode_set = set()

for freq, coords in antennas.items():
    if len(coords) < 2:
        continue

    n = len(coords)
    for i in range(n):
        Ax, Ay = coords[i]
        for j in range(i + 1, n):
            Bx, By = coords[j]

            dx = Bx - Ax
            dy = By - Ay
            g = gcd(dx, dy)
            dx //= g
            dy //= g

            x_cur, y_cur = Ax, Ay
            if 0 <= x_cur < cols and 0 <= y_cur < rows:
                antinode_set.add((x_cur, y_cur))

            while True:
                x_cur += dx
                y_cur += dy
                if not (0 <= x_cur < cols and 0 <= y_cur < rows):
                    break
                antinode_set.add((x_cur, y_cur))

            x_cur, y_cur = Ax, Ay
            while True:
                x_cur -= dx
                y_cur -= dy
                if not (0 <= x_cur < cols and 0 <= y_cur < rows):
                    break
                antinode_set.add((x_cur, y_cur))

print(len(antinode_set))
