from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

rules = []

i = 0

while dat[i] != "":
    rules.append(dat[i])
    i += 1

valids = set()

for line in rules:
    second = line.split(": ")[1]
    ranges = second.split(" or ")
    for r in ranges:
        low, high = r.split("-")
        low = int(low)
        high = int(high)
        for n in range(low, high + 1):
            valids.add(n)

i = dat.index("nearby tickets:") + 1
nearby = []

while i < len(dat):
    nearby.append(dat[i])
    i += 1

error = 0

for line in nearby:
    nums = line.split(",")
    for n in nums:
        n = int(n)
        if n not in valids:
            error += n

print(error)
