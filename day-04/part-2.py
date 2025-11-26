from pathlib import Path


def count_x_mas(grid):
    rows = len(grid)
    cols = len(grid[0])
    counter = 0

    def pair_ok(a, b):
        return (a == "M" and b == "S") or (a == "S" and b == "M")

    def is_valid(x, y):
        if not (0 < x < rows - 1 and 0 < y < cols - 1):
            return False

        tl, tr = grid[x - 1][y - 1], grid[x - 1][y + 1]
        bl, br = grid[x + 1][y - 1], grid[x + 1][y + 1]

        return pair_ok(tl, br) and pair_ok(tr, bl)

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == "A" and is_valid(x, y):
                counter += 1

    return counter


def load_grid():
    grid = []
    with Path("input.txt").open() as file:
        for line in file:
            grid.append(list(line.strip()))
    return grid


grid = load_grid()
count = count_x_mas(grid)
print(count)
