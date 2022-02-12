from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")


def parse(ins, cx, cy, dx, dy):
    ch = ins[0]
    num = int(ins[1:])
    if ch == "F":
        cx += dx * num
        cy += dy * num
    elif ch == "N":
        dy += num
    elif ch == "S":
        dy -= num
    elif ch == "E":
        dx += num
    elif ch == "W":
        dx -= num
    elif ch == "L" and num == 90 or ch == "R" and num == 270:
        dx, dy = -dy, dx
    elif ch == "L" and num == 270 or ch == "R" and num == 90:
        dx, dy = dy, -dx
    elif ch == "L" and num == 180 or ch == "R" and num == 180:
        dx, dy = -dx, -dy
    return cx, cy, dx, dy


cx, cy, dx, dy = 0, 0, 10, 1

for line in dat:
    cx, cy, dx, dy = parse(line, cx, cy, dx, dy)

print(abs(cx) + abs(cy))
