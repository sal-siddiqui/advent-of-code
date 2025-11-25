import re
from pathlib import Path

pattern = re.compile(r"mul\((\d+),(\d+)\)")
contents = Path("input.txt").read_text()
matches = re.findall(pattern, contents)

total = 0
for left, right in matches:
    total += int(left) * int(right)

print(total)
