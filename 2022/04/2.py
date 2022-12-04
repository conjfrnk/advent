from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

count = 0

for line in dat:
    both = line.split(",")
    one = both[0].split("-")
    two = both[1].split("-")
    min1 = int(one[0])
    max1 = int(one[1])
    min2 = int(two[0])
    max2 = int(two[1])
    if max1 < min2 or min2 > max1 or max2 < min1 or min1 > max2:
        continue
    count += 1

print(count)
