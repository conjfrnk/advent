from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

windows = []

for i in range(len(dat) - 2):
    windows.append(0)
    for j in range(3):
        windows[-1] += int(dat[i + j])

prev = None
larger = 0

for line in windows:
    curr = int(line)
    if prev is not None and curr > prev:
        larger += 1
    prev = curr

print(larger)
