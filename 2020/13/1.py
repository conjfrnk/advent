from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

earliest = int(dat[0])
busses = []

for bus in dat[1].split(","):
    if bus != "x":
        busses.append(int(bus))

possible = []

for bus in busses:
    test = bus
    while test < earliest:
        test += bus
    possible.append((bus, test))

possible.sort(key=lambda x: x[1])

wait = possible[0][1] - earliest
print(wait * possible[0][0])
