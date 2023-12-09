from pathlib import Path
import math

fn = "ex3.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

instructions = dat[0]
instructions = [c for c in instructions]

graph = dict()

nodes = []

for i in range(2, len(dat)):
    node, steps = dat[i].split("=")
    node = node.strip()
    steps = steps.strip().split(", ")
    steps[0] = steps[0][1:]
    steps[1] = steps[1][:-1]
    graph[node] = steps
    if node[-1] == "A":
        nodes.append(node)

lengths = []

for node in nodes:
    i = 0
    steps = 0
    while node[-1] != "Z":
        if i == len(instructions):
            i = 0
        node = graph[node][0 if instructions[i] == "L" else 1]
        i += 1
        steps += 1
    lengths.append(steps)

print(math.lcm(*lengths))
