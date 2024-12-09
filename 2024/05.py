# ADVENT-OF-CODE 2024
# Jour 5
# https://adventofcode.com/2024/day/5

# --- Day 5: Print Queue ---

with open('input/05.txt', 'r') as file:

    rule_positions = {}
    updates = []
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        if '|' in line:
            line = line.split('|')
            page_x = int(line[0])
            page_y = int(line[1])
            if page_x in rule_positions.keys():
                rule_positions[page_x].append(page_y)
            else:
                rule_positions[page_x] = [page_y]

        if ',' in line:
            updates.append([int(x) for x in line.split(',')])

def is_valid_update(update):
    for i, page in enumerate(update):
        if page in rule_positions.keys():
            for previous_page in update[:i]:
                if previous_page in rule_positions[page]:
                    return False
    return True

def sort_update(update):
    sorted_update = []
    update_rule_positions = {}
    filtered_rule_positions = {}

    for page in update:
        update_rule_positions[page] = rule_positions[page]

    for page, dependencies in update_rule_positions.items():
        filtered_rule_positions[page] = [dependency for dependency in dependencies if dependency in update]

    for k in range(0, len(update)):
        for page, dependencies in filtered_rule_positions.items():
            if len(dependencies) == k:
                sorted_update.append(page)

    return sorted_update

good_sum = 0
bad_sum = 0

for update in updates:
    if is_valid_update(update):
        good_sum += update[len(update) // 2]
    else:
        new_update = sort_update(update)
        bad_sum += new_update[len(new_update) // 2]

print(f'Partie 1 : {good_sum}')
print(f'Partie 2 : {bad_sum}')
