# ADVENT-OF-CODE 2024
# Jour 18
# https://adventofcode.com/2024/day/18

# --- Day 18: RAM Run ---

walls = []

with open("../inputs/18.txt") as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        line = line.strip()
        line = line.split(",")
        walls.append((int(line[0]), int(line[1])))

y_max = 71
x_max = 71
start = (0, 0)
stop = (x_max - 1, y_max - 1)

def find_shortest_path(walls):

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def is_valid(x, y):
        return 0 <= x < x_max and 0 <= y < y_max and (x, y) not in walls

    queue = [(0, 0)]
    distances = [[-1 for _ in range(x_max)] for _ in range(y_max)]
    parents = [[None for _ in range(x_max)] for _ in range(y_max)]
    distances[0][0] = 0

    while queue:
        x, y = queue.pop(0)

        for dx, dy in directions:
            x2, y2 = x + dx, y + dy
            if is_valid(x2, y2) and distances[x2][y2] == -1:
                distances[x2][y2] = distances[x][y] + 1
                parents[x2][y2] = (x, y)
                queue.append((x2, y2))

        if (x, y) == (x_max - 1, y_max - 1):
            path = reconstruct_path(parents, x_max - 1, y_max - 1)
            return distances[x][y], path

    return -1, [-10, -10]

def reconstruct_path(parents, x, y):
    path = []
    while (x, y) != (0, 0):
        path.append((x, y))
        x, y = parents[x][y]
    path.reverse()
    return path

ans, path = find_shortest_path(walls[:1024])

print(f"Part 1 : {ans}")

def draw_map(walls, path, to_highlight):
    for y in range(0, y_max):
        line = ""
        for x in range(0, x_max):
            if to_highlight and (x, y) in to_highlight:
                line += "\033[33m@\033[0m"
            elif (x, y) in walls:
                line += "\033[32m#\033[0m"
            elif (x, y) in path:
                line += "\033[31mO\033[0m"
            else:
                line += "."
        print(line)

draw_map(walls[:1024], path, [])

# Partie 2

l = len(walls)
last_number_steps, last_path = find_shortest_path(walls[:1024])

for k in range(1024 + 1, l):
    if walls[k - 1] in last_path:
        walls_to_test = walls[:k]
        last_number_steps, last_path = find_shortest_path(walls_to_test)
        if last_number_steps == -1:
            print(f"Part 2 : {','.join(str(x) for x in walls_to_test[-1])}")
            break

walls_to_test = walls[:k - 1]
_, last_path1 = find_shortest_path(walls_to_test)
draw_map(walls_to_test, last_path1, [])

print("\n")

walls_to_test = walls[:k]
_, last_path = find_shortest_path(walls_to_test)
print(walls[k - 1])
draw_map(walls_to_test, last_path, [walls[k - 1]])
