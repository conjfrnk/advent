from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

best = 0

for i in range(1, len(dat) - 1):
    for j in range(1, len(dat[i]) - 1):
        curr = int(dat[i][j])
        score = 1
        new = 0
        for t in dat[i][:j][::-1]:
            new += 1
            if int(t) >= curr:
                break
        score *= new
        new = 0
        for t in dat[i][j + 1 :]:
            new += 1
            if int(t) >= curr:
                break
        score *= new
        new = 0
        for t in [dat[di][j] for di in range(i)][::-1]:
            new += 1
            if int(t) >= curr:
                break
        score *= new
        new = 0
        for t in [dat[di][j] for di in range(i + 1, len(dat[0]))]:
            new += 1
            if int(t) >= curr:
                break
        score *= new
        if score > best:
            best = score

print(best)
