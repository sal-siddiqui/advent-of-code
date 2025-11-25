import re
from pathlib import Path

pattern = re.compile(r"(do\(\)|don't\(\))" + r"|" + r"mul\((\d+),(\d+)\)")
contents = Path("input.txt").read_text()
matches = re.findall(pattern, contents)

enable = True
total = 0
for instruction, left, right in matches:
    if instruction == "do()":
        enable = True
    elif instruction == "don't()":
        enable = False
    elif enable:
        total += int(left) * int(right)


print(total)
