# ADVENT-OF-CODE 2024
# Jour 6
# https://adventofcode.com/2024/day/6

# --- Day 6: Guard Gallivant ---

obstacles = []
guard_pos = (0, 0)

with open('06.txt') as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        line = line.strip()
        for j, case in enumerate(line) :
            if case == '#':
                obstacles.append((i, j))
            if case == '^':
                guard_pos = (i, j)

    Y_MAX = len(lines)
    X_MAX = len(lines[0])

def turn_right(dir):
    if dir == (-1, 0): return 0, 1
    if dir == (0, 1): return 1, 0
    if dir == (1, 0): return 0, -1
    if dir == (0, -1): return -1, 0


# Partie 1

x_guard = guard_pos[0]
y_guard = guard_pos[1]
visited_pos = set()
dir = (-1, 0) # up

while 0 <= x_guard < X_MAX and 0 <= y_guard < Y_MAX:
    if (x_guard + dir[0], y_guard + dir[1]) in obstacles:
        dir = turn_right(dir)
    else :
        x_guard += dir[0]
        y_guard += dir[1]
        visited_pos.add((x_guard, y_guard))

print(f"Partie 1 : {len(visited_pos) - 1}")

# Partie 2

x_guard = guard_pos[0]
y_guard = guard_pos[1]
visited_pos = set()
visited_pos_dir = set()
dir = (-1, 0) # up

loops = 0


def loop_possible(x_guard, y_guard, dir, visited_pos):
    new_obstacle = x_guard + dir[0], y_guard + dir[1]

    visited_for_test = visited_pos.copy()

    while 0 <= x_guard < X_MAX and 0 <= y_guard < Y_MAX:

        if (x_guard + dir[0], y_guard + dir[1]) in obstacles or (x_guard + dir[0], y_guard + dir[1]) == new_obstacle:
            dir = turn_right(dir)

        else:
            x_guard += dir[0]
            y_guard += dir[1]

            if (x_guard, y_guard, dir) in visited_for_test:
                return True

            visited_for_test.add((x_guard, y_guard, dir))

    return False


while 0 <= x_guard < X_MAX and 0 <= y_guard < Y_MAX:
    if (x_guard + dir[0], y_guard + dir[1]) in obstacles:
        dir = turn_right(dir)
    else:
        if not (x_guard + dir[0], y_guard + dir[1]) in visited_pos:
            if loop_possible(x_guard, y_guard, dir, visited_pos):
                loops += 1
        x_guard += dir[0]
        y_guard += dir[1]
        visited_pos_dir.add((x_guard, y_guard, dir))
        visited_pos.add((x_guard, y_guard))

print(f"Partie 2 : {loops}")