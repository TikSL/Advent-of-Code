# ADVENT-OF-CODE 2021
# Jour 01
# https://adventofcode.com/2021/day/1

print(f'# ------------------------------------------------ #')
print(f'#             Advent Of Code 2021 - 01             #')
print(f'#                 Balayage du sonar                #')
print(f'# ------------------------------------------------ #\n')

# ------------------- Partie 1 ------------------- #
print(f'# ------------------- Partie 1 ------------------- #')

with open('../inputs/01.txt', 'r') as fichier:
    lignes = fichier.readlines()
    profondeur1 = int(lignes[0][:-1])
    compteur_plus_profond = 0
    for ligne in lignes[1:]:
        profondeur2 = int(ligne[:-1])
        if profondeur2 > profondeur1:
            compteur_plus_profond += 1
        profondeur1 = profondeur2

fichier.close()

print(f'Le sonar a mesuré {compteur_plus_profond} descentes.')

# ------------------- Partie 2 ------------------- #
print(f'# ------------------- Partie 2 ------------------- #')

with open('../inputs/01.txt', 'r') as fichier:
    lignes = fichier.readlines()

    compteur_plus_profond = 0

    somme1 = int(lignes[0][:-1]) + int(lignes[1][:-1]) + int(lignes[2][:-1])

    n = len(lignes)
    for k in range(1, n-2):
        somme2 = int(lignes[k][:-1]) + int(lignes[k+1][:-1]) + int(lignes[k+2][:-1])

        if somme2 > somme1:
            compteur_plus_profond += 1

        somme1 = somme2

fichier.close()

print(f'Avec une fenêtre glissante, le sonar mesure {compteur_plus_profond} descentes.')
