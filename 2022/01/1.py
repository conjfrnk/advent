from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

elves = []

elf = 0
for line in dat:
    if line == "":
        elves.append(elf)
        elf = 0
        continue
    elf += int(line)

print(max(elves))
