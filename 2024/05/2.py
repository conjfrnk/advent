from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

line_break_idx = dat.index("")
rules = dat[:line_break_idx]
updates = dat[line_break_idx + 1 :]

rules_parsed = []
for r in rules:
    x, y = r.split("|")
    x = int(x)
    y = int(y)
    rules_parsed.append((x, y))

bad_updates = []
for u in updates:
    pages = [int(x) for x in u.split(",")]
    for x, y in rules_parsed:
        if x in pages and y in pages:
            if pages.index(x) > pages.index(y):
                bad_updates.append(pages)
                break


def topo_sort(nodes, edges):
    from collections import defaultdict, deque

    g = defaultdict(list)
    indeg = {n: 0 for n in nodes}
    for a, b in edges:
        g[a].append(b)
        indeg[b] += 1
    q = deque([n for n in nodes if indeg[n] == 0])
    res = []
    while q:
        cur = q.popleft()
        res.append(cur)
        for nxt in g[cur]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return res


fixed_bad_updates = []
for pages in bad_updates:
    pages_set = set(pages)
    relevant_rules = [
        (x, y) for (x, y) in rules_parsed if x in pages_set and y in pages_set
    ]
    sorted_pages = topo_sort(pages, relevant_rules)
    fixed_bad_updates.append(sorted_pages)

answer_part2 = sum(u[len(u) // 2] for u in fixed_bad_updates)
print(answer_part2)
