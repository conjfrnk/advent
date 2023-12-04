from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

total = 0

for line in dat:
    win, have = line.split("|")
    win = win.split(":")[1].strip()
    win = win.split(" ")
    winning = set()
    for num in win:
        if num != "" and int(num) not in winning:
            winning.add(int(num))
    have = have.split(" ")
    score = 0
    for num in have:
        if num != "" and int(num) in winning:
            if score == 0:
                score = 1
            else:
                score *= 2
    total += score

print(total)
