# ADVENT-OF-CODE 2022
# Jour 11
# https://adventofcode.com/2022/day/11

print(f'# ------------------------------------------------ #')
print(f'#             Advent Of Code 2022 - 11             #')
print(f'#               Monkey in the Middle               #')
print(f'# ------------------------------------------------ #\n')

# ------------------- Partie 1 ------------------- #
print(f'# ------------------- Partie 1 ------------------- #')

Singes = [[93, 98], [95, 72, 98, 82, 86], [85, 62, 82, 86, 70, 65, 83, 76], [86, 70, 71, 56], [77, 71, 86, 52, 81, 67], [89, 87, 60, 78, 54, 77, 98], [69, 65, 63], [89]]
compteur = [0 for _ in range(8)]


def tour():

    compteur_tour = [0 for _ in range(8)]

    for item in Singes[0]:
        compteur_tour[0] += 1
        item *= 17
        item //= 3
        if item % 19 == 0:
            Singes[5].append(item)
        else:
            Singes[3].append(item)
    Singes[0] = []

    for item in Singes[1]:
        compteur_tour[1] += 1
        item += 5
        item //= 3
        if item % 17 == 0:
            Singes[7].append(item)
        else:
            Singes[6].append(item)
    Singes[1] = []

    for item in Singes[2]:
        compteur_tour[2] += 1
        item += 8
        item //= 3
        if item % 13 == 0:
            Singes[3].append(item)
        else:
            Singes[0].append(item)
    Singes[2] = []

    for item in Singes[3]:
        compteur_tour[3] += 1
        item += 1
        item //= 3
        if item % 7 == 0:
            Singes[4].append(item)
        else:
            Singes[5].append(item)
    Singes[3] = []

    for item in Singes[4]:
        compteur_tour[4] += 1
        item += 4
        item //= 3
        if item % 17 == 0:
            Singes[1].append(item)
        else:
            Singes[6].append(item)
    Singes[4] = []

    for item in Singes[5]:
        item *= 7
        item //= 3
        if item % 2 == 0:
            Singes[1].append(item)
        else:
            Singes[4].append(item)
    Singes[5] = []

    for item in Singes[6]:
        compteur_tour[6] += 1
        item += 6
        item //= 3
        if item % 3 == 0:
            Singes[7].append(item)
        else:
            Singes[2].append(item)
    Singes[6] = []

    for item in Singes[7]:
        compteur_tour[7] += 1
        item = item ** 2
        item //= 3
        if item % 11 == 0:
            Singes[0].append(item)
        else:
            Singes[2].append(item)
    Singes[7] = []

    return compteur_tour


for _ in range(20):

    incr = tour()
    for k in range(8):
        compteur[k] += incr[k]

compteur.sort(reverse=True)

print(compteur[0] * compteur[1])

# ------------------- Partie 2 ------------------- #
print(f'# ------------------- Partie 2 ------------------- #')