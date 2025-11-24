from pathlib import Path

left_list = []
right_list = []

with Path("input.txt").open("r") as file:
    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

similarity_score = 0
for num in left_list:
    count = right_list.count(num)
    similarity_score += num * count

print(similarity_score)
