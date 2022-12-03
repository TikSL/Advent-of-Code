# ADVENT-OF-CODE 2022
# Jour 1
# https://adventofcode.com/2022/day/1


print(f'# ------------------------------------------------ #')
print(f'#             Advent Of Code 2022 - 01             #')
print(f'#                     Calories                     #')
print(f'# ------------------------------------------------ #\n')


# ------------------- Partie 1 ------------------- #
print(f'# ------------------- Partie 1 ------------------- #')

lutins = [0]

with open('01.txt', 'r') as fichier:
    lignes = fichier.readlines()
    for ligne in lignes:
        texte = ligne[:-1]
        if texte == '':
            lutins.append(0)
        else:
            calorie = int(texte)
            lutins[len(lutins) - 1] += calorie

fichier.close()

lutins.sort()
print(f'Le lutin le plus chargé à {max(lutins)} calories.')

# ------------------- Partie 2 ------------------- #
print(f'# ------------------- Partie 2 ------------------- #')

lutins.sort()
somme_calorie = sum(lutins[-3:])
print(f'Total des calories des 3 premiers lutins : {somme_calorie}.')


