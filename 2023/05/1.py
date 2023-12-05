from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n\n")

seeds = list(map(int, dat[0].split()[1:]))

rules = dict()

for rule in dat[1:]:
    lines = rule.split("\n")
    k, v = lines[0], []
    for line in lines[1:]:
        v.append(tuple(map(int, line.split())))
    k = k.split()[0]
    f, t = k.split("-to-")
    rules[f, t] = v

ctype = "seed"
sequence = [ctype]

while ctype != "location":
    ntype = None
    for f, t in rules:
        if f == ctype:
            ntype = t
    sequence.append(ntype)
    ctype = ntype

ans = max(seeds)
for seed in seeds:
    seq = sequence[:]
    new = None
    while len(seq) > 1:
        f = seq.pop(0)
        t = seq[0]
        rule = rules[f, t]

        new = None

        for d, s, r in rule:
            if s <= seed < s + r:
                new = d + (seed - s)

        if new is None:
            new = seed

        seed = new

    if new < ans:
        ans = new

print(ans)
