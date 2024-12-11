# ADVENT-OF-CODE 2023
# Jour 11
# https://adventofcode.com/2023/day/11

# --- Day 11: Cosmic Expansion ---

# Partie 1

lines = open('../inputs/11.txt', 'r').readlines()

univers = []
for line in lines:
    line = line.strip()
    if '#' in line :
        univers.append([x for x in line])
    else:
        univers.append([x for x in line])
        univers.append([x for x in line])


def colonne_vide(univers, i_col):
    for x in range(len(univers)):
        if univers[x][i_col] == "#":
            return False
    return True

liste_col = []

n = len(univers[0])
for i_col in range(n):
    if colonne_vide(univers, i_col):
        liste_col.append(i_col)


univers_final = []
for x in univers:
    ligne_univers_final = []
    for i, y in enumerate(x):
        if i in liste_col:
            ligne_univers_final.append(".")
        ligne_univers_final.append(y)
    univers_final.append(ligne_univers_final)

liste_coord_galaxies = []
for y in range(len(univers_final)):
    for x in range(len(univers_final[0])):
        if univers_final[y][x] == "#":
            liste_coord_galaxies.append((x,y))

somme = 0
while len(liste_coord_galaxies)>0:
    galaxieA = liste_coord_galaxies[0]
    for galaxieB in liste_coord_galaxies[1:]:
        xA = galaxieA[0]
        yA = galaxieA[1]
        xB = galaxieB[0]
        yB = galaxieB[1]
        distance = abs(xA - xB) + abs(yA - yB)
        somme += distance
    liste_coord_galaxies = liste_coord_galaxies[1:]

print(somme)

# Partie 2

univers= []

compteur = 0
for line in lines:
    line = line.strip()
    line_univ_y = []
    if "#" in line:
        compteur += 1
    else:
        compteur += 1000000
    for x in line:
        if x == ".":
            line_univ_y.append(None)
        else:
            line_univ_y.append((0, compteur))
    univers.append(line_univ_y)


def colonne_vide(univers, i_col):
    for x in range(len(univers)):
        if univers[x][i_col] is not None:
            return False
    return True

liste_col = []

n = len(univers[0])
for i_col in range(n):
    if colonne_vide(univers, i_col):
        liste_col.append(i_col)


univers_final = []

for x in univers:
    compteur = 0
    ligne_univers_final = []
    for i, y in enumerate(x):
        if i in liste_col:
            compteur += 1000000
        else:
            compteur += 1
        if y is not None:
            ligne_univers_final.append((compteur, y[1]))
        else:
            ligne_univers_final.append(y)
    univers_final.append(ligne_univers_final)

liste_coord_galaxies = []
for y in range(len(univers_final)):
    for x in range(len(univers_final[0])):
        if univers_final[y][x] is not None:
            liste_coord_galaxies.append(univers_final[y][x])

for x in univers_final:
    print(x)

somme = 0
while len(liste_coord_galaxies)>0:
    galaxieA = liste_coord_galaxies[0]
    for galaxieB in liste_coord_galaxies[1:]:
        xA = galaxieA[0]
        yA = galaxieA[1]
        xB = galaxieB[0]
        yB = galaxieB[1]
        distance = abs(xA - xB) + abs(yA - yB)
        somme += distance
    liste_coord_galaxies = liste_coord_galaxies[1:]

print(somme)



