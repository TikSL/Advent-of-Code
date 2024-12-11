# ADVENT-OF-CODE 2024
# Jour 1
# https://adventofcode.com/2024/day/1

# --- Day 1: Historian Hysteria ---

sum_tot = 0
liste_droite = []
liste_gauche = []
with open('input/01.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line[:-1]
        l = line.split(f" ")
        g = l[0]
        d = l[len(l)-1]

        liste_gauche.append(int(g))
        liste_droite.append(int(d))

    liste_gauche.sort()
    liste_droite.sort()
    for i in range(len(liste_gauche)):
        diff = abs(liste_gauche[i] - liste_droite[i])
        sum_tot += diff

    print("Partie 1 : ",sum_tot)

# --- Part Two ---

somme = 0
liste_droite = []
liste_gauche = []
with open('input/01.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line[:-1]
        l = line.split(f" ")
        g = l[0]
        d = l[len(l)-1]

        liste_gauche.append(int(g))
        liste_droite.append(int(d))

    for x in liste_gauche:

        somme += liste_droite.count(x)*x

    print("Partie 2 : ",somme)
