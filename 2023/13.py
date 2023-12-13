# ADVENT-OF-CODE 2023
# Jour 13
# https://adventofcode.com/2023/day/13

# --- Day 13: Point of Incidence ---

lines = open('13.txt', 'r').readlines()

patterns = []
pattern = []

for line in lines:
    line = line.strip()
    if line == '':
        patterns.append(pattern)
        pattern = []
    else:
        pattern.append(line)
patterns.append(pattern)


# Partie 1 :

def verifier_symetrie(pattern, i):
    n = min(len(pattern) - i - 1, i + 1)
    for k in range(0, n):
        if pattern[i - k] != pattern[i + k + 1]:
            return False
    return True


def trouver_ligne_symetrie(pattern):
    for i in range(0, len(pattern) - 1):

        if verifier_symetrie(pattern, i):
            return i + 1
    return 0


def trouver_colonne_symetrie(pattern):
    pattern_translate = []
    for x in range(len(pattern[0])):
        ligne = ""
        for y in range(len(pattern)):
            ligne += pattern[y][x]
        pattern_translate.append(ligne)
    return trouver_ligne_symetrie(pattern_translate)


somme = 0
for pattern in patterns:
    somme += trouver_colonne_symetrie(pattern) + 100 * (trouver_ligne_symetrie(pattern))
print(f"Partie 1 : {somme}")


# Partie 2:

def compter_diff(liste1, liste2):
    cpt = 0
    for i in range(len(liste1)):
        if liste1[i] != liste2[i]:
            cpt += 1
    return cpt


def verifier_symetrie_part2(pattern, i):
    n = min(len(pattern) - i - 1, i + 1)
    compteur_diff = 0
    for k in range(0, n):
        compteur_diff += compter_diff(pattern[i - k], pattern[i + k + 1])
        if compteur_diff > 1:
            return False
    if compteur_diff == 1:
        return True
    return False


def trouver_ligne_symetrie_part2(pattern):
    for i in range(0, len(pattern) - 1):
        if verifier_symetrie_part2(pattern, i):
            return i + 1
    return 0


def trouver_colonne_symetrie_part2(pattern):
    pattern_translate = []
    for x in range(len(pattern[0])):
        ligne = ""
        for y in range(len(pattern)):
            ligne += pattern[y][x]
        pattern_translate.append(ligne)
    return trouver_ligne_symetrie_part2(pattern_translate)


somme = 0
for pattern in patterns:
    somme += trouver_colonne_symetrie_part2(pattern) + 100 * (trouver_ligne_symetrie_part2(pattern))
print(f"Partie 2 : {somme}")
