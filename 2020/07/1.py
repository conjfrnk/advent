from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

lu = dict()

for line in dat:
    bag, cont = line.split(" contain ")
    bag = bag.split(" bag")[0]
    lu[bag] = set()
    conts = cont.split("bag")
    for c in conts:
        end = len(c) - 1
        if c[0].isdigit():
            lu[bag].add(c[2:end])
        elif c[0:2] == ", ":
            lu[bag].add(c[4:end])
        elif c[0:2] == "s,":
            lu[bag].add(c[5:end])


def search(d, b):
    if b == "shiny gold":
        return 0
    else:
        for b2 in d[b]:
            if b2 == "shiny gold" or search(d, b2) == 1:
                return 1
    return 0


n = 0
for b in lu:
    n += search(lu, b)
print(n)
