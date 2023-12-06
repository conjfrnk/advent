from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

times = dat[0].split(":")[1].strip().split(" ")
time = ""
for t in times:
    if t != "":
        time += t
time = int(time)

dists = dat[1].split(":")[1].strip().split(" ")
dist = ""
for d in dists:
    if d != "":
        dist += d
dist = int(dist)

ans = 1

record = dist
count = 0
for holding in range(time + 1):
    movetime = time - holding
    speed = holding
    dist = movetime * speed
    if dist > record:
        count += 1
ans *= count

print(ans)
