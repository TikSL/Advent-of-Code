# ADVENT-OF-CODE 2024
# Jour 14
# https://adventofcode.com/2024/day/14

# --- Day 14: Restroom Redoubt ---

robots = []
with open("../inputs/14.txt") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        line = line.split()
        line[0] = line[0].replace('p=', '').split(',')
        line[1] = line[1].replace('v=', '').split(',')
        line[0] = [int(x) for x in line[0]]
        line[1] = [int(x) for x in line[1]]
        robots.append([line[0], line[1]])

seconds = 100
x_max = 101
y_max = 103

for s in range(seconds):
    for i, robot in enumerate(robots):
        print(i, robot)
        #print(type(x) for x in robot)
        x = robot[0][0]
        y = robot[0][1]
        vx = robot[1][0]
        vy = robot[1][1]
        x2, y2 = x+vx, y+vy
        x2 = x2 % x_max
        y2 = y2 % y_max
        robots[i][0][0] = x2
        robots[i][0][1] = y2


print("######")
q1, q2, q3, q4 = 0, 0, 0, 0
for robot in robots:
    x = robot[0][0]
    y = robot[0][1]
    if x < x_max//2 and y < y_max//2:
        q1 += 1
    elif x > x_max//2 and y < y_max//2:
        q2 += 1
    elif x < x_max//2 and y > y_max//2:
        q3 += 1
    elif x > x_max//2 and y > y_max//2:
        q4 += 1

print(q1, q2, q3, q4)
print(f"Partie 1 : {q1 * q2* q3* q4}")
print(f"Partie 2 : {0}")
