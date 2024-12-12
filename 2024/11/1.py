from pathlib import Path

# fn = "ex2.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

stones = []
for line in dat:
    stones.extend(line.split())


def transform(stones):
    new_stones = []
    for s in stones:
        if s == "0":
            new_stones.append("1")
        else:
            length = len(s)
            if length % 2 == 0:
                half = length // 2
                left = str(int(s[:half]))
                right = str(int(s[half:]))
                new_stones.append(left)
                new_stones.append(right)
            else:
                val = int(s)
                val *= 2024
                new_stones.append(str(val))
    return new_stones


for _ in range(25):
    stones = transform(stones)

print(len(stones))
