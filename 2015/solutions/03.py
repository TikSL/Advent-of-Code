# ADVENT-OF-CODE 2015
# Jour 3
# https://adventofcode.com/2015/day/3

# --- Day 3: Perfectly Spherical Houses in a Vacuum ---

# Partie 1

lines = open('../inputs/03.txt', 'r').readlines()

x, y = 0, 0
maisons = []
for caractere in lines[0]:
    if caractere == ">":
        x += 1
    elif caractere == "<":
        x -= 1
    elif caractere == "^":
        y += 1
    elif caractere == "v":
        y -= 1
    maisons.append((x,y))

nbr_maisons_uniques = len(set(maisons))

print(f'Partie 1 : {nbr_maisons_uniques}')

# Partie 2

def nouv_coord(x, y, caractere):
    if caractere == ">":
        x += 1
    elif caractere == "<":
        x -= 1
    elif caractere == "^":
        y += 1
    elif caractere == "v":
        y -= 1
    return x, y

xs, ys, xr, yr = 0, 0, 0, 0
maisons = []
for i, caractere in enumerate(lines[0]):
    if i%2 == 1:
        xs, ys = nouv_coord(xs, ys, caractere)
        maisons.append((xs,ys))
    else :
        xr, yr = nouv_coord(xr, yr, caractere)
        maisons.append((xr, yr))
nbr_maisons_uniques = len(set(maisons))

print(f'Partie 2 : {nbr_maisons_uniques}')
