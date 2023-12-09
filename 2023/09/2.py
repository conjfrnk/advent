from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

ans = 0

for oasis in dat:
    diffs = []
    diffs.append([int(i.strip()) for i in oasis.split()])
    while sum(diffs[-1]) != 0:
        d = []
        for i in range(1, len(diffs[-1])):
            d.append(diffs[-1][i] - diffs[-1][i - 1])
        diffs.append(d)
    print(diffs)
    diffs[-1].insert(0, 0)
    for i in range(2, len(diffs) + 1):
        j = len(diffs) - i
        diffs[j].insert(0, diffs[j][0] - diffs[j + 1][0])
    print(diffs)
    ans += diffs[0][0]

print(ans)
