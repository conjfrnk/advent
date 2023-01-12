from pathlib import Path
from copy import deepcopy

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

LENGTH = 2

ref = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0),
}


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return x


seen = set()
tail = [(0, 0) for _ in range(LENGTH)]
for d, num in [(i.split(' ')[0], int(i.split(' ')[1])) for i in dat]:
    for _ in range(num):
        new_tail = deepcopy(tail)
        for i in range(LENGTH):
            tail_pos = tail[i]
            if i == 0:
                new_tail[0] = tuple(sum(i) for i in zip(tail_pos, ref[d]))
            else:
                old = new_tail[i - 1]
                flag = False
                for t in [(x, y) for y in range(-1, 2) for x in range(-1, 2)]:
                    if old == tuple(sum(i) for i in zip(tail_pos, t)):
                        flag = True
                        break
                if not flag:
                    new_tail[i] = tuple(
                        sum(i) for i in
                        zip(tail_pos, (sign(old[0] - tail_pos[0]),
                                       sign(old[1] - tail_pos[1])))
                    )

        tail = deepcopy(new_tail)
        seen.add(tail[-1])

print(len(seen))
