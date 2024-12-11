# ADVENT-OF-CODE 2021
# Jour 02
# https://adventofcode.com/2021/day/2

print(f'# ------------------------------------------------ #')
print(f'#             Advent Of Code 2021 - 02             #')
print(f'#                     Plongez !                    #')
print(f'# ------------------------------------------------ #\n')

# ------------------- Partie 1 ------------------- #
print(f'# ------------------- Partie 1 ------------------- #')

pos_horiz = 0
pos_vert = 0

with open('../inputs/02.txt', 'r') as fichier:
    lignes = fichier.readlines()
    for ligne in lignes:
        ordre = ligne[:-1].split(' ')
        if ordre[0] == 'up':
            pos_vert += - int(ordre[1])
        elif ordre[0] == 'down':
            pos_vert += int(ordre[1])
        else:
            pos_horiz += int(ordre[1])

fichier.close()

print(f'Position horizontale : {pos_horiz}\n'
      f'Position verticale : {pos_vert}\n'
      f'Facteur : {pos_vert * pos_horiz}')

# ------------------- Partie 2 ------------------- #
print(f'# ------------------- Partie 2 ------------------- #')

pos_horiz = 0
pos_vert = 0
aim = 0

with open('../inputs/02.txt', 'r') as fichier:
    lignes = fichier.readlines()
    for ligne in lignes:
        ordre = ligne[:-1].split(' ')
        if ordre[0] == 'up':
            aim += - int(ordre[1])
        elif ordre[0] == 'down':
            aim += int(ordre[1])
        else:
            pos_horiz += int(ordre[1])
            pos_vert += int(ordre[1]) * aim

fichier.close()

print(f'Position horizontale : {pos_horiz}\n'
      f'Position verticale : {pos_vert}\n'
      f'Facteur : {pos_vert * pos_horiz}')
