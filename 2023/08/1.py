from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

instructions = dat[0]
instructions = [c for c in instructions]

graph = dict()

for i in range(2, len(dat)):
    node, steps = dat[i].split("=")
    node = node.strip()
    steps = steps.strip().split(", ")
    steps[0] = steps[0][1:]
    steps[1] = steps[1][:-1]
    graph[node] = steps

curr = "AAA"
i = 0
steps = 0

while curr != "ZZZ":
    if i == len(instructions):
        i = 0
    curr = graph[curr][0 if instructions[i] == "L" else 1]
    i += 1
    steps += 1

print(steps)
