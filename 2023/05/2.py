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

sequences = []

for a, b in zip(seeds[::2], seeds[1::2]):
    ranges = [range(a, a + b)]
    seq = sequence[:]
    while len(seq) > 1:
        f = seq.pop(0)
        t = seq[0]
        rule = rules[f, t]

        nranges = []

        for rang in ranges:
            nvals = []
            while len(rang) > 0:
                flag = False
                best = len(rang)

                for d, s, r in rule:
                    if s <= rang[0] < s + r:
                        sep = rang[0] - s
                        ns = d + sep
                        nlen = min(r - sep, len(rang))
                        nvals.append(range(ns, ns + nlen))
                        rang = rang[nlen:]
                        flag = True
                        break
                    elif s < rang[0]:
                        sep = rang[0] - s
                        best = min(best, sep)
                if not flag:
                    nvals.append(rang[:best])
                    rang = rang[best:]
            nranges += nvals
        ranges = nranges
    sequences += ranges

print(min(cr.start for cr in sequences))
