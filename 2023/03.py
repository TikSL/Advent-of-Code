# ADVENT-OF-CODE 2023
# Jour 3
# https://adventofcode.com/2023/day/3

# --- Day 3: Gear Ratios ---

# Partie 1

lines = open('03.txt', 'r').readlines()

for i in range(len(lines)):
    lines[i] = "." + lines[i].strip() + "."
k = len(lines[0])
lines = ["."*k] + lines + ["."*k]


def recuperer_nbr_ligne(ligne: str):
    nombres = []
    i = 0
    n = len(ligne)
    while i < n:
        nombre_dec = []
        if ligne[i].isdigit():
            index = i
            k = 0
            while i < n and ligne[i].isdigit():
                nombre_dec.append(ligne[i])
                i += 1
                k += 1
            nombre = 0

            for chiffre in nombre_dec:
                nombre = nombre * 10 + int(chiffre)
            nombres.append((index, nombre))
        i += 1
    return nombres


def est_valide(nbr, index_nbr, numero_ligne, matrice):
    taille_nbr = len(str(nbr))
    for i in range(-1, 2):
        for j in range(-1, taille_nbr+1):
            if matrice[numero_ligne+i][index_nbr+j] in "$&#-+=@/%*":
                return True
    return False


somme = 0

for i, line in enumerate(lines):
    nombres = recuperer_nbr_ligne(line)

    for nombre in nombres:
        if est_valide(nombre[1], nombre[0], i, lines):
            somme += nombre[1]

print(f"Partie 1 : {somme}")

# Partie 2:


def trouver_voisins(x, y):
    voisins = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if lines[x+i][y+j].isdigit():
                voisins.append(nombre(x+i, y+j))
    return list(set(voisins))


def nombre(x, y):
    nombre = []
    i = 0
    while lines[x][y+i] not in ".*":
        nombre.append(lines[x][y+i])
        i += 1
    i = 1
    while lines[x][y-i] not in ".*":
        nombre = [lines[x][y-i]] + nombre
        i += 1
    nbr = 0
    for chiffre in nombre:
        nbr = nbr * 10 + int(chiffre)
    return nbr


ratio = 0
for i, line in enumerate(lines):
    for j, case in enumerate(line):
        if case == '*':

            nbr_voisins = trouver_voisins(i, j)
            if len(nbr_voisins) == 2:
                ratio += nbr_voisins[0] * nbr_voisins[1]

print(f"Partie 2 : {ratio}")
