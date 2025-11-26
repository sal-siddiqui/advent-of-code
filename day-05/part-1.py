def parse(file_path):
    with open(file_path, "r") as file:
        content = file.read().strip()

    rules_part, updates_part = content.split("\n\n")

    # Parse rules: X must come before Y
    rules = []
    for line in rules_part.splitlines():
        x, y = line.split("|")
        rules.append((int(x), int(y)))

    # Parse updates: lists of page numbers
    updates = []
    for line in updates_part.splitlines():
        updates.append([int(page) for page in line.split(",")])

    return rules, updates


def solve(rules, updates):
    total = 0

    for update in updates:
        # Create position map for quick lookups
        position = {page: i for i, page in enumerate(update)}

        # Check if all rules are satisfied
        is_valid = True
        for x, y in rules:
            # Only check if both pages exist in this update
            if x in position and y in position:
                if position[x] > position[y]:  # x should come before y
                    is_valid = False
                    break

        # Add middle page if valid
        if is_valid:
            total += update[len(update) // 2]

    return total


file_path = "input.txt"
rules, updates = parse(file_path)
result = solve(rules, updates)
print(result)
