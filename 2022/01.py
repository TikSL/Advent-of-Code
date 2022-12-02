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

calories_max = max(lutins)
index_lutin_max = lutins.index(calories_max)

print(f'Lutin le plus chargé : {index_lutin_max + 1} avec {calories_max} calories.')

# ------------------- Partie 2 ------------------- #
print(f'# ------------------- Partie 2 ------------------- #')

somme_calorie = 0
for k in range(3):
    calories_max = max(lutins)
    somme_calorie += calories_max
    index_lutin_max = lutins.index(calories_max)
    print(f'Lutin {k+1} le plus chargé : {index_lutin_max + 1} avec {calories_max} calories.')
    lutins = lutins[:index_lutin_max] + lutins[index_lutin_max+1:]
print(f'Total des calories des 3 premiers lutins : {somme_calorie}.')


