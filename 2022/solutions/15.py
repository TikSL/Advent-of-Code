# ADVENT-OF-CODE 2022
# Jour 15
# https://adventofcode.com/2022/day/15

print(f'# ------------------------------------------------ #')
print(f'#             Advent Of Code 2022 - 15             #')
print(f'#             .             #')
print(f'# ------------------------------------------------ #\n')

# ------------------- Partie 1 ------------------- #
print(f'# ------------------- Partie 1 ------------------- #')

with open('test.txt', 'r') as fichier:
    lignes = fichier.readlines()
    couples_SB = []
    for ligne in lignes:
        affichage = ligne[:-1].split(' ')
        x_s = int(affichage[2][2:-1])
        y_s = int(affichage[3][2:-1])
        x_b = int(affichage[8][2:-1])
        y_b = int(affichage[9][2:])
        couples_SB.append(((x_s, y_s), (x_b, y_b)))

    min_largeur, max_largeur = -2, 25
    min_hauteur, max_hauteur = 0, 22

    largeur = max_largeur - min_largeur
    hauteur = max_hauteur - min_hauteur

    carte_recherche = [['.' for _ in range(largeur+1)] for _ in range(hauteur+1)]

    for (s, b) in couples_SB:
        sx, sy, bx, by = s[0], s[1], b[0], b[1]
        carte_recherche[sy-min_hauteur][sx-min_largeur] = 'S'
        carte_recherche[by-min_hauteur][bx-min_largeur] = 'B'

        distance_manhattan = abs(sx-bx) + abs(sy-by)

        for x in range(sx-distance_manhattan, sx+distance_manhattan):
            for y in range(sy-distance_manhattan, sy+distance_manhattan):
                carte_recherche[y][x] = '#'

    for ligne in carte_recherche:
        print(''.join(k for k in ligne))




# ------------------- Partie 2 ------------------- #
print(f'# ------------------- Partie 2 ------------------- #')
