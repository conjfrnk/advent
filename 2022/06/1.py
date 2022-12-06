from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

line = dat[0]
req = 4

for i in range(req, len(line)):
    check = line[i - req : i]
    if len(set(check)) == len(check):
        print(i)
        break
