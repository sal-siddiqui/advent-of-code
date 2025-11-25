# Geneic implementation of dfs
# Requirements:
# "XMAS"[index]
# explore in a single chosen direction
# return True if you matched all 4 letters
# Base case: out of bounds
# move one step further in the same direction


from pathlib import Path


def out_of_bounds(r, c):
    return 0 <= r < H and 0 <= c < W


def dfs(r, c, index, dr, dc):
    if out_of_bounds(r, c):
        return False

    if grid[r][c] != word[index]:
        return False

    # 2. success case
    if index == len(word) - 1:
        return True

    # 3. explore neighbors
    return dfs(r + dr, c + dc, index + 1, dr, dc)


grid = []
with Path("input.txt").open("r") as file:
    for line in file:
        grid.append([line.strip()])


word = "XMAS"
H = len(grid)
W = len(grid[0])

count = 0

directions = [
    (-1, 0),  # up
    (1, 0),  # down
    (0, -1),  # left
    (0, 1),  # right
    (-1, -1),  # up-left
    (-1, 1),  # up-right
    (1, -1),  # down-left
    (1, 1),  # down-right
]

for r in range(H):
    for c in range(W):
        if grid[r][c] != "X":
            continue

        for dr, dc in directions:
            if dfs(r, c, 0, dr, dc):
                count += 1

print(count)
