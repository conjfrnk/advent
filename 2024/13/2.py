from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = [d for d in open(fn).read().strip().split("\n") if d.strip()]

offset = 10000000000000

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
    xT = int(lineP[1][2:].strip(",")) + offset
    yT = int(lineP[2][2:]) + offset
    machines.append((xA, yA, xB, yB, xT, yT))

results = []
for xA, yA, xB, yB, xT, yT in machines:
    D = xA * yB - yA * xB
    if D == 0:
        continue
    numA = xT * yB - yT * xB
    numB = xA * yT - yA * xT
    if numA % D != 0 or numB % D != 0:
        continue
    a = numA // D
    b = numB // D
    if a < 0 or b < 0:
        continue
    cost = 3 * a + b
    results.append(cost)

print(sum(results) if results else 0)
