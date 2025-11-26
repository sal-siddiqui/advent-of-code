from pathlib import Path


def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])

    count = 0

    directions = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]

    for x in range(rows):
        gx = grid[x]
        for y in range(cols):
            if gx[y] != "X":
                continue

            for dx, dy in directions:
                x1, y1 = x + dx, y + dy
                x2, y2 = x1 + dx, y1 + dy
                x3, y3 = x2 + dx, y2 + dy

                # Bounds check
                if not (0 <= x3 < rows and 0 <= y3 < cols):
                    continue

                # Char check
                if grid[x1][y1] == "M" and grid[x2][y2] == "A" and grid[x3][y3] == "S":
                    count += 1

    return count


def load_grid():
    grid = []
    with Path("input.txt").open() as file:
        for line in file:
            grid.append(list(line.strip()))
    return grid


grid = load_grid()
count = count_xmas(grid)
print(count)

# Time (r * c)
# If rows and collumns are counted as just chars and char = n then O(n)
# Space O(n)
