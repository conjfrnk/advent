from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

charlist = []

for line in dat:
    chars = line.split(" ")
    charlist.append(chars)

total = 0

for line in charlist:
    score = 0
    you = line[1]
    opp = line[0]
    if you == "X":
        score += 1
    elif you == "Y":
        score += 2
    elif you == "Z":
        score += 3
    if opp == "A" and you == "Y":
        score += 6
    elif opp == "A" and you == "X":
        score += 3
    elif opp == "B" and you == "Z":
        score += 6
    elif opp == "B" and you == "Y":
        score += 3
    elif opp == "C" and you == "X":
        score += 6
    elif opp == "C" and you == "Z":
        score += 3
    total += score

print(total)
