# ADVENT-OF-CODE 2023
# Jour 4
# https://adventofcode.com/2023/day/4

# --- Day 4: Scratchcards ---

# Partie 1

lines = open('04.txt', 'r').readlines()
cartes = []
for line in lines:
    carte = line.split(":")[1]
    carte = carte.replace("\n", "")
    carte = carte.split("|")
    pts_gagnants = []
    pts_carte = []

    for elt in carte[0].split(" "):
        if elt.isdigit():
            pts_gagnants.append(int(elt))
    for elt in carte[1].split(" "):
        if elt.isdigit():
            pts_carte.append(int(elt))

    cartes.append((pts_gagnants, pts_carte))

somme = 0
for carte in cartes:
    nbr_ok = 0
    for pt_gagnant in carte[0]:
        for pt_carte in carte[1]:
            if pt_gagnant == pt_carte:
                nbr_ok += 1
    if nbr_ok != 0:
        somme += 2**(nbr_ok - 1)

print(somme)


# Partie 2

somme = 0
nbr_cartes = [1 for k in range(len(cartes))]

for i, carte in enumerate(cartes):
    nbr_ok = 0
    for pt_gagnant in carte[0]:
        for pt_carte in carte[1]:
            if pt_gagnant == pt_carte:
                nbr_ok += 1
    if nbr_ok != 0:
        somme += nbr_cartes[i]
        for k in range(nbr_ok):
            nbr_cartes[i + 1 + k] += nbr_cartes[i]
print(sum(nbr_cartes))