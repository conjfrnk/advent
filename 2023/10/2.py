from pathlib import Path

fn = "ex5.txt"
#fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

start = []

found = False

for i in range(len(dat)):
    for j in range(len(dat[i])):
        if dat[i][j] == "S":
            start.append((i, j))
            found = True
            break
    if found:
        break

i, j = start[0][0], start[0][1]
print(start)
ends = []
# find initial dirs
found = 2
if dat[i - 1][j] in {"F", "7", "|"}:
    if found > 0:
        ends.append((i - 1, j))
        found -= 1
if dat[i + 1][j] in {"|", "J", "L"}:
    if found > 0:
        ends.append((i + 1, j))
        found -= 1
if dat[i][j - 1] in {"F", "L", "-"}:
    if found > 0:
        ends.append((i, j - 1))
        found -= 1
if dat[i][j + 1] in {"-", "7", "J"}:
    if found > 0:
        ends.append((i, j + 1))
        found -= 1

ends = [ends[0]], [ends[1]]
seen = [start[0], ends[0][0], ends[1][0]]
print(seen)

while ends[0][-1] != ends[1][-1]:
    for e in range(len(ends)):
        i, j = ends[e][-1][0], ends[e][-1][1]
        curr = dat[i][j]
        if curr in {"-", "J", "7"}:
            if dat[i][j - 1] in {"F", "L", "-"}:
                if (i, j - 1) not in seen:
                    ends[e].append((i, j - 1))
                    seen.append((i, j - 1))
                    continue
                elif (i, j - 1) == seen[-1]:
                    ends[e].append((i, j - 1))
                    break
        if curr in {"-", "F", "L"}:
            if dat[i][j + 1] in {"J", "7", "-"}:
                if (i, j + 1) not in seen:
                    ends[e].append((i, j + 1))
                    seen.append((i, j + 1))
                    continue
                elif (i, j + 1) == seen[-1]:
                    ends[e].append((i, j + 1))
                    break
        if curr in {"|", "J", "L"}:
            if dat[i - 1][j] in {"F", "7", "|"}:
                if (i - 1, j) not in seen:
                    ends[e].append((i - 1, j))
                    seen.append((i - 1, j))
                    continue
                elif (i - 1, j) == seen[-1]:
                    ends[e].append((i - 1, j))
                    break
        if curr in {"|", "F", "7"}:
            if dat[i + 1][j] in {"J", "L", "|"}:
                if (i + 1, j) not in seen:
                    ends[e].append((i + 1, j))
                    seen.append((i + 1, j))
                    continue
                elif (i + 1, j) == seen[-1]:
                    ends[e].append((i + 1, j))
                    break


in_loop = 0
inside = []

for i in range(len(dat)):
    looped = False
    for j in range(len(dat[i])):
        if (i, j) in seen:
            if looped and dat[i][j] in {"|", "J", "7"}:
                looped = False
                continue
            if not looped and dat[i][j] in {"|", "L", "F", "S"}:
                if dat[i][j - 1] not in {"|", "J", "7"}:
                    looped = True
                    continue
        if looped and dat[i][j] == ".":
            print((i, j))
            inside.append((i, j))
            in_loop += 1

for i in range(len(dat)):
    for j in range(len(dat[i])):
        if (i, j) in seen:
            print(dat[i][j], end="")
        elif (i, j) in inside:
            print("I", end="")
        else:
            print(".", end="")
    print()

print(in_loop)
