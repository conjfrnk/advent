from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

if fn.name == "ex1.txt":
    WIDTH = 11
    HEIGHT = 7
else:
    WIDTH = 101
    HEIGHT = 103

TIME = 100

mid_x = WIDTH // 2
mid_y = HEIGHT // 2

robots = []
for line in dat:
    part_p, part_v = line.split(" v=")
    px, py = part_p[2:].split(",")
    vx, vy = part_v.split(",")

    px = int(px)
    py = int(py)
    vx = int(vx)
    vy = int(vy)
    robots.append((px, py, vx, vy))

counts = [0, 0, 0, 0]  # Q1, Q2, Q3, Q4

for px, py, vx, vy in robots:
    nx = (px + vx * TIME) % WIDTH
    ny = (py + vy * TIME) % HEIGHT

    if nx == mid_x or ny == mid_y:
        continue
    if nx < mid_x and ny < mid_y:
        counts[0] += 1  # Q1
    elif nx > mid_x and ny < mid_y:
        counts[1] += 1  # Q2
    elif nx < mid_x and ny > mid_y:
        counts[2] += 1  # Q3
    elif nx > mid_x and ny > mid_y:
        counts[3] += 1  # Q4

answer = 1
for c in counts:
    answer *= c

print(answer)
