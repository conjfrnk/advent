from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

prev = None
larger = 0

for line in dat:
    curr = int(line)
    if prev is not None and curr > prev:
        larger += 1
    prev = curr

print(larger)
