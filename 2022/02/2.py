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
        score += 0
        if opp == "A":
            score += 3
        elif opp == "B":
            score += 1
        elif opp == "C":
            score += 2
    elif you == "Y":
        score += 3
        if opp == "A":
            score += 1
        elif opp == "B":
            score += 2
        elif opp == "C":
            score += 3
    elif you == "Z":
        score += 6
        if opp == "A":
            score += 2
        elif opp == "B":
            score += 3
        elif opp == "C":
            score += 1
    total += score

print(total)
