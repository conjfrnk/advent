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
            lu[bag].add((int(c[0]), c[2:end]))
        elif c[0:2] == ", ":
            lu[bag].add((int(c[2]), c[4:end]))
        elif c[0:2] == "s,":
            lu[bag].add((int(c[3]), c[5:end]))

print(lu, end="\n\n")


def search(db, bn, sta, ct):
    global n

    sta.append(ct)
    prod = 1
    for i in sta:
        prod *= i
    n += prod

    if len(db[bn]) == 0:
        return

    for b in db[bn]:
        search(db, b[1], sta[:], b[0])


n = 0
search(lu, "shiny gold", [], 1)
n -= 1
print(n)
