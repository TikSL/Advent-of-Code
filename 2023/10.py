# ADVENT-OF-CODE 2023
# Jour 10
# https://adventofcode.com/2023/day/10

# --- Day 10: Pipe Maze ---

lines = open('10.txt', 'r').readlines()

carte = []
carte.append([None for _ in range(len(lines[0]))])
xs, ys = 0, 0

y = 0
for line in lines:
    line = line.strip()
    x = 0
    ligne_carte = []
    for caracter in line:
        if caracter == '.':
            ligne_carte.append(None)
        elif caracter == "-":
            ligne_carte.append([(x-1,y), (x+1,y)])
        elif caracter == "|":
            ligne_carte.append([(x,y-1), (x,y+1)])
        elif caracter == "L":
            ligne_carte.append([(x,y-1), (x+1,y)])
        elif caracter == "7":
            ligne_carte.append([(x-1, y), (x, y+1)])
        elif caracter == "F":
            ligne_carte.append([(x+1, y), (x, y+1)])
        elif caracter == "J":
            ligne_carte.append([(x, y-1), (x-1, y)])
        elif caracter == "S":
            xs, ys = x, y
            ligne_carte.append((True, True))
        x += 1
    carte.append([None] + ligne_carte + [None])
    y += 1
carte.append([None for _ in range(len(lines[0]))])


def verifier(x, y, xydep, xyarr):
    [x_dep, y_dep] = xydep
    [x_arr, y_arr] = xyarr
    if True in [x,y,x_dep,y_dep]:
        return True
    if carte[x_dep][y_dep][1] != (x,y):
        return False
    elif carte[y_arr][x_arr][0] != (x,y):
        return False
    else:
        return True

carte_simplifiee = []

y_max = len(carte)
x_max = len(carte[0])

for y in range(y_max):
    ligne_carte_simplifiee = []
    for x in range(x_max):
        if carte[y][x] == None:
            ligne_carte_simplifiee.append(".")
        elif verifier(x, y, carte[x][y][0], carte[x][y][1]):
            ligne_carte_simplifiee.append(lines[y-1][x-1])
        else:
            ligne_carte_simplifiee.append(".")
    carte_simplifiee.append(ligne_carte_simplifiee)

for ligne in carte_simplifiee:
    print(ligne)

