from pathlib import Path


def is_safe(nums):
    nums = list(nums)

    is_increasing = True
    is_decreasing = True

    for i in range(len(nums) - 1):
        a, b = nums[i], nums[i + 1]
        diff = abs(b - a)

        if diff < 1 or diff > 3:
            return False

        if b > a:
            is_decreasing = False

        if b < a:
            is_increasing = False

    return is_increasing or is_decreasing


def problem_dampener(nums):
    nums = list(nums)

    if is_safe(nums):
        return True

    for i in range(len(nums)):
        new_list = nums[:i] + nums[i + 1 :]
        if is_safe(new_list):
            return True

    return False


# def is_safe(nums):
#     nums = list(nums)
#     diffs = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]

#     # Check all differences are between 1 and 3 in magnitude
#     if not all(1 <= abs(d) <= 3 for d in diffs):
#         return False

#     all_increasing = all(d > 0 for d in diffs)
#     all_decreasing = all(d < 0 for d in diffs)

#     return all_increasing or all_decreasing


count = 0
with Path("input.txt").open("r") as file:
    for line in file:
        nums = map(int, line.split())
        if problem_dampener(nums):
            count += 1

print(count)
