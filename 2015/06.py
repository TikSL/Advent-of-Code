# ADVENT-OF-CODE 2015
# Jour 6
# https://adventofcode.com/2015/day/6

# --- Day 6: Probably a Fire Hazard ---

# Partie 1

lines = open('06.txt', 'r').readlines()

def recup_instructions(lines):
    instructions = []

    for line in lines:
        instructions_ligne = []
        line = line.replace("\n", "")
        line = line.replace("through", "")
        line = line.replace("turn on", "on")
        line = line.replace("turn off", "of")
        line = line.replace("toggle", "to")
        line = line.split(" ")
        instructions_ligne.append(line[0])
        for code in line[1:]:
            if not code == "":
                x,y = code.split(",")
                instructions_ligne.append((int(x),int(y)))
        instructions.append(instructions_ligne)
    return instructions


instructions = recup_instructions(lines)

matrice = [[0 for _ in range(1000)] for _ in range(1000)]


def set_matrice(matrice, x_debut, y_debut, x_fin, y_fin, valeur):
    for x in range(x_debut, x_fin+1):
        for y in range(y_debut, y_fin+1):
            matrice[y][x] = valeur
    return matrice


def set_matrice_toggle(matrice, x_debut, y_debut, x_fin, y_fin):
    for x in range(x_debut, x_fin+1):
        for y in range(y_debut, y_fin+1):
            if matrice[y][x] == 0:
                matrice[y][x] = 1
            else:
                matrice[y][x] = 0
    return matrice

for instruction in instructions:
    x_debut = instruction[1][0]
    y_debut = instruction[1][1]

    x_fin = instruction[2][0]
    y_fin = instruction[2][1]

    if instruction[0] == "on":
        matrice = set_matrice(matrice, x_debut, y_debut, x_fin, y_fin, 1)
    elif instruction[0] == "of":
        matrice = set_matrice(matrice, x_debut, y_debut, x_fin, y_fin, 0)
    elif instruction[0] == "to":
        matrice = set_matrice_toggle(matrice, x_debut, y_debut, x_fin, y_fin)

somme = 0
for ligne in matrice:
    somme += sum(ligne)

print(f"Partie 1 : {somme}")


# Partie 2

def set_matrice_part2(matrice, x_debut, y_debut, x_fin, y_fin, valeur):
    for x in range(x_debut, x_fin+1):
        for y in range(y_debut, y_fin+1):
            matrice[y][x] += valeur
            if matrice[y][x] < 0:
                matrice[y][x] = 0
    return matrice

matrice = [[0 for _ in range(1000)] for _ in range(1000)]

for instruction in instructions:
    x_debut = instruction[1][0]
    y_debut = instruction[1][1]

    x_fin = instruction[2][0]
    y_fin = instruction[2][1]

    if instruction[0] == "on":
        matrice = set_matrice_part2(matrice, x_debut, y_debut, x_fin, y_fin, 1)
    elif instruction[0] == "of":
        matrice = set_matrice_part2(matrice, x_debut, y_debut, x_fin, y_fin, -1)
    elif instruction[0] == "to":
        matrice = set_matrice_part2(matrice, x_debut, y_debut, x_fin, y_fin,2)

somme = 0
for ligne in matrice :
    somme += sum(ligne)
print(f"Partie 2 : {somme}")
