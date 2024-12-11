# ADVENT-OF-CODE 2022
# Jour 04
# https://adventofcode.com/2022/day/4

print(f'# ------------------------------------------------ #')
print(f'#             Advent Of Code 2022 - 04             #')
print(f'#                     Nettoyage                    #')
print(f'# ------------------------------------------------ #\n')

# ------------------- Partie 1 ------------------- #
print(f'# ------------------- Partie 1 ------------------- #')

recouvrements = 0

with open('../inputs/04.txt', 'r') as fichier:
    lignes = fichier.readlines()

    for ligne in lignes:

        lutin1 = [int(x) for x in ligne[:-1].split(',')[0].split('-')]
        lutin2 = [int(x) for x in ligne[:-1].split(',')[1].split('-')]

        if (lutin1[0] <= lutin2[0] and lutin2[1] <= lutin1[1]) or (lutin2[0] <= lutin1[0] and lutin1[1] <= lutin2[1]):
            recouvrements += 1

fichier.close()
print(f'Il y a {recouvrements} recouvrements.')


# ------------------- Partie 2 ------------------- #
print(f'# ------------------- Partie 2 ------------------- #')

recouvrements_partiels = 0

with open('../inputs/04.txt', 'r') as fichier:
    lignes = fichier.readlines()

    for ligne in lignes:

        lutin1 = [int(x) for x in ligne[:-1].split(',')[0].split('-')]
        lutin2 = [int(x) for x in ligne[:-1].split(',')[1].split('-')]

        if (lutin1[0] <= lutin2[0] <= lutin1[1]) or (lutin2[0] <= lutin1[0] <= lutin2[1]):
            recouvrements_partiels += 1

fichier.close()
print(f'Il y a {recouvrements_partiels} recouvrements partiels.')
