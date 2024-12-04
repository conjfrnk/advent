from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

grid = [list(line.strip()) for line in dat if line.strip()]

count = 0

rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0

sequences = ["MAS", "SAM"]

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "A":
            for diag1 in sequences:
                for diag2 in sequences:
                    match_diag1 = True
                    positions_diag1 = [(i - 1, j - 1), (i, j), (i + 1, j + 1)]
                    for idx in range(3):
                        x, y = positions_diag1[idx]
                        if (
                            x < 0
                            or x >= rows
                            or y < 0
                            or y >= cols
                            or grid[x][y] != diag1[idx]
                        ):
                            match_diag1 = False
                            break

                    match_diag2 = True
                    positions_diag2 = [(i - 1, j + 1), (i, j), (i + 1, j - 1)]
                    for idx in range(3):
                        x, y = positions_diag2[idx]
                        if (
                            x < 0
                            or x >= rows
                            or y < 0
                            or y >= cols
                            or grid[x][y] != diag2[idx]
                        ):
                            match_diag2 = False
                            break

                    if match_diag1 and match_diag2:
                        count += 1

print(count)
