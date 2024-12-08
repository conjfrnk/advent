from pathlib import Path

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
    n = len(coords)
    if n < 2:
        continue

    for i in range(n):
        Ax, Ay = coords[i]
        for j in range(i + 1, n):
            Bx, By = coords[j]

            P1x = 2 * Ax - Bx
            P1y = 2 * Ay - By
            P2x = 2 * Bx - Ax
            P2y = 2 * By - Ay

            if 0 <= P1y < rows and 0 <= P1x < cols:
                antinode_set.add((P1x, P1y))
            if 0 <= P2y < rows and 0 <= P2x < cols:
                antinode_set.add((P2x, P2y))

print(len(antinode_set))
