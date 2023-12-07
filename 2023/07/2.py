from pathlib import Path
import collections

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")


def proc(hand):
    hand2 = ["J23456789TQKA".index(i) for i in hand]
    types = []
    for r in "23456789TQKA":
        c = collections.Counter(hand.replace("J", r))
        p = tuple(sorted(c.values()))
        t = [
            (1, 1, 1, 1, 1),
            (1, 1, 1, 2),
            (1, 2, 2),
            (1, 1, 3),
            (2, 3),
            (1, 4),
            (5,),
        ].index(p)
        types.append(t)
    return (max(types), *hand2)


hand = sorted((proc(h), int(b)) for h, b in (l.split() for l in dat))
ans = 0
for i, (_, b) in enumerate(hand):
    ans += (i * b) + b

print(ans)
