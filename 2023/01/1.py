from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

letters = "abcdefghijklmnopqrstuvwxyz"
ans = 0

for line in dat:
    for l in letters:
        line = line.replace(l, "")
    ans += int(line[0]) * 10 + int(line[-1])

print(ans)
