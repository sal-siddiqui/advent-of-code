from pathlib import Path

left_list = []
right_list = []

with Path("input.txt").open("r") as file:
    for line in file:
        numbers = line.split()
        left, right = map(int, numbers)
        left_list.append(left)
        right_list.append(right)


right_count = {}
for num in right_list:
    if num in right_count:
        right_count[num] += 1
    else:
        right_count[num] = 1

similarity_score = 0
for num in left_list:
    if num in right_count:
        similarity_score += num * right_count[num]


print(similarity_score)
