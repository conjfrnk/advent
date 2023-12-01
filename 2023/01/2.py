from pathlib import Path

# fn = "ex2.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

nums = list(enumerate("0123456789")) + \
       list(enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]))

ans = 0

def first(line, kv):
    for i in range(len(line)):
        for k, v in kv:
            if line[i:].startswith(v):
                return k

for line in dat:
    num = first(line, nums) * 10 + first(line[::-1], [(k, v[::-1]) for (k, v) in nums])
    ans += num

print(ans)
