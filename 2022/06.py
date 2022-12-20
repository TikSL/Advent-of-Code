# ADVENT-OF-CODE 2022
# Jour 06
# https://adventofcode.com/2022/day/6

print(f'# ------------------------------------------------ #')
print(f'#             Advent Of Code 2022 - 06             #')
print(f'#                  Tuning Trouble                  #')
print(f'# ------------------------------------------------ #\n')

# ------------------- Partie 1 ------------------- #
print(f'# ------------------- Partie 1 ------------------- #')

with open('06.txt', 'r') as fichier:
    signal = fichier.readlines()[0][:-1]

    liste = []
    compteur = 0
    while len(liste) < 5:
        lettre = signal[compteur]
        while lettre in liste:
            liste.remove(liste[0])
        liste.append(lettre)
        compteur += 1
    print(compteur - 1)


# ------------------- Partie 2 ------------------- #
print(f'# ------------------- Partie 2 ------------------- #')

with open('06.txt', 'r') as fichier:
    signal = fichier.readlines()[0][:-1]

    liste = []
    compteur = 0
    while len(liste) < 14:
        lettre = signal[compteur]
        while lettre in liste:
            liste.remove(liste[0])
        liste.append(lettre)
        compteur += 1
    print(compteur)
