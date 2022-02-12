from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")


def to_dir(r):
    while r < 0:
        r += 360
    while r >= 360:
        r -= 360
    if r == 90:
        return "E"
    elif r == 180:
        return "S"
    elif r == 270:
        return "W"
    elif r == 0:
        return "N"


def parse(ins, x, y, r):
    ch = ins[0]
    num = int(ins[1:])
    if ch == "N":
        y += num
    elif ch == "S":
        y -= num
    elif ch == "E":
        x += num
    elif ch == "W":
        x -= num
    elif ch == "L":
        r -= num
    elif ch == "R":
        r += num
    elif ch == "F":
        ins = to_dir(r) + str(num)
        x, y, r = parse(ins, x, y, r)
    return x, y, r


x, y, r = 0, 0, 90

for line in dat:
    x, y, r = parse(line, x, y, r)

print(abs(x) + abs(y))
