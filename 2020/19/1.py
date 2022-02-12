from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
rules, tests = open(fn).read().strip().split("\n\n")

dr = {}
for r in rules.split("\n"):
    rn, val = r.split(": ")
    dr[int(rn)] = val


def consume(x, rn):
    rule = dr[rn]
    if rule[0] == '"':
        # terminal symbol
        rule = rule.strip('"')
        if x.startswith(rule):
            return len(rule)
        else:
            return -1
    for opt in rule.split(" | "):
        acc = 0
        for rn in opt.split(" "):
            rn = int(rn)
            ret = consume(x[acc:], rn)
            if ret == -1:
                acc = -1
                break
            acc += ret
        if acc != -1:
            return acc
    return -1


acc = 0
for x in tests.split("\n"):
    acc += consume(x, 0) == len(x)
print(acc)
