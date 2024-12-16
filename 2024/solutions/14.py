# ADVENT-OF-CODE 2024
# Jour 14
# https://adventofcode.com/2024/day/14

# --- Day 14: Restroom Redoubt ---

robots = []
with open("../inputs/14.txt") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip().split()
        pos = [int(x) for x in line[0].replace('p=', '').split(',')]
        vel = [int(x) for x in line[1].replace('v=', '').split(',')]
        robots.append([pos, vel])

x_max = 101
y_max = 103

seconds = 100
for _ in range(seconds):
    for robot in robots:
        x, y = robot[0]
        vx, vy = robot[1]
        robot[0][0] = (x + vx) % x_max
        robot[0][1] = (y + vy) % y_max

q1, q2, q3, q4 = 0, 0, 0, 0
for robot in robots:
    x, y = robot[0]
    if x < x_max//2 and y < y_max//2:
        q1 += 1
    elif x > x_max//2 and y < y_max//2:
        q2 += 1
    elif x < x_max//2 and y > y_max//2:
        q3 += 1
    elif x > x_max//2 and y > y_max//2:
        q4 += 1

print(f"Partie 1 : {q1 * q2* q3* q4}")

# Partie 2
def dessiner(robots_positions):
    grid = [[' ' for _ in range(x_max)] for _ in range(y_max)]
    for x, y in robots_positions:
        grid[y][x] = '#'
    print("\n".join("".join(row) for row in grid))


s = 0
nbr_robots_aligned = 10 # Enough to detect a tree
found = False
while not found:
    s2 = s
    s += 1

    for robot in robots:
        x, y = robot[0]
        vx, vy = robot[1]
        robot[0][0] = (x + vx) % x_max
        robot[0][1] = (y + vy) % y_max

    robot_positions = [(robot[0][0], robot[0][1]) for robot in robots]

    for x, y in robot_positions:
        if all((x, y + l) in robot_positions for l in range(nbr_robots_aligned)):
            print(f"Partie 2 : {s+100}") # 100 in part 1
            dessiner(robot_positions)
            found = True
            break
