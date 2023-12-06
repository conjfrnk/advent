from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

times = [int(i) for i in dat[0].split(":")[1].strip().split(" ") if i != ""]
distances = [int(i) for i in dat[1].split(":")[1].strip().split(" ") if i != ""]
ans = 1

for i, time in enumerate(times):
    record = distances[i]
    count = 0
    for holding in range(time + 1):
        movetime = time - holding
        speed = holding
        dist = movetime * speed
        if dist > record:
            count += 1
    ans *= count

print(ans)
