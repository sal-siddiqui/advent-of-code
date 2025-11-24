from pathlib import Path

left_list = []
right_list = []

with Path("input.txt").open("r") as file:
    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

left_list.sort()
right_list.sort()

total_distance = 0

for left, right in zip(left_list, right_list):
    total_distance += abs(left - right)

print(total_distance)
