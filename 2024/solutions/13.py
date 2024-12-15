# ADVENT-OF-CODE 2024
# Jour 13
# https://adventofcode.com/2024/day/13

# --- Day 13: Claw Contraption ---

with open("../inputs/13.txt") as file:
    lines = file.readlines()
    i = 0
    dict= {}
    for line in lines:
        line = line.strip()
        if "Button A" in line:
            line = line.strip("Button A : ")
            line = line.split(", ")
            line = [int(k.split("+")[1]) for k in line]
            dict[i] = [line]
        elif "Button B" in line:
            line = line.strip("Button B : ")
            line = line.split(", ")
            line = [int(k.split("+")[1]) for k in line]
            dict[i].append(line)
        elif "Prize" in line:
            line = line.strip("Prize : ")
            line = line.split(", ")
            line = [int(k.split("=")[1]) for k in line]
            dict[i].append(line)
            i+=1

sum = 0

for key in dict.keys():

    machine = dict[key]
    buttonAX = machine[0][0]
    buttonAY = machine[0][1]
    buttonBX = machine[1][0]
    buttonBY = machine[1][1]
    prizeX = machine[2][0]
    prizeY = machine[2][1]

    for i in range(100):
        for j in range(100):
            if i * buttonAX + j * buttonBX == prizeX and i * buttonAY + j * buttonBY == prizeY:
                sum += 3 * i + j
                break

print(f"Partie 1 : {sum}")


# Partie 2
# nsm on fait des maths

def solve_equation(ax, bx, px, ay, by, py):

    determinant = ax * by - ay * bx

    if determinant == 0:
        return 0, 0

    x = (px * by - py * bx) / determinant
    y = (ax * py - ay * px) / determinant
    if x.is_integer() and y.is_integer():
        return int(x), int(y)
    else:
        return 0, 0

sum2 = 0
for key in dict.keys():

    machine = dict[key]
    buttonAX = machine[0][0]
    buttonAY = machine[0][1]
    buttonBX = machine[1][0]
    buttonBY = machine[1][1]
    prizeX = machine[2][0] + 10000000000000
    prizeY = machine[2][1] + 10000000000000

    px, py = solve_equation(buttonAX, buttonBX, prizeX, buttonAY, buttonBY, prizeY)

    sum2 += 3 * px + py

print(f"Partie 2 : {sum2}")