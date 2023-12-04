from pathlib import Path
from collections import defaultdict

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

winnings = defaultdict(int)

for i, line in enumerate(dat):
    winnings[i] += 1
    win, have = line.split("|")
    card, win = win.split(":")
    card = card.split(" ")[1].strip()
    win = win.strip().split(" ")
    winning = set()
    for num in win:
        if num != "" and int(num) not in winning:
            winning.add(int(num))
    have = have.split(" ")
    matches = 0
    for num in have:
        if num != "" and int(num) in winning:
            matches += 1
    for j in range(matches):
        winnings[i + 1 + j] += winnings[i]

print(winnings)
ans = 0

for card in winnings:
    ans += winnings[card]

print(ans)
