from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = [d for d in open(fn).read().strip().split("\n") if d.strip()]

if len(dat) % 3 != 0:
    raise ValueError("Input not multiple of 3 lines")

machines = []
for i in range(0, len(dat), 3):
    lineA = dat[i].split()
    lineB = dat[i + 1].split()
    lineP = dat[i + 2].split()
    xA = int(lineA[2][2:].strip(","))
    yA = int(lineA[3][2:])
    xB = int(lineB[2][2:].strip(","))
    yB = int(lineB[3][2:])
    xT = int(lineP[1][2:].strip(","))
    yT = int(lineP[2][2:])
    machines.append((xA, yA, xB, yB, xT, yT))

results = []
for xA, yA, xB, yB, xT, yT in machines:
    best = None
    for a in range(101):
        for b in range(101):
            if a * xA + b * xB == xT and a * yA + b * yB == yT:
                cost = 3 * a + b
                if best is None or cost < best:
                    best = cost
    if best is not None:
        results.append(best)

print(sum(results) if results else 0)
