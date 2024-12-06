from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

line_break_idx = dat.index("")
rules = dat[:line_break_idx]
updates = dat[line_break_idx + 1 :]

rules_parsed = []
for r in rules:
    x, y = r.split("|")
    x = int(x)
    y = int(y)
    rules_parsed.append((x, y))

answer = 0
for u in updates:
    pages = [int(x) for x in u.split(",")]
    good = True
    for x, y in rules_parsed:
        if x in pages and y in pages:
            if pages.index(x) > pages.index(y):
                good = False
                break
    if good:
        answer += pages[len(pages) // 2]

print(answer)
