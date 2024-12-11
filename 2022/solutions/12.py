# ADVENT-OF-CODE 2022
# Jour 12
# https://adventofcode.com/2022/day/12

print(f'# ------------------------------------------------ #')
print(f'#             Advent Of Code 2022 - 12             #')
print(f'#              Hill Climbing Algorithm             #')
print(f'# ------------------------------------------------ #\n')

# ------------------- Partie 1 ------------------- #
print(f'# ------------------- Partie 1 ------------------- #')

liste_hauteurs = 'abcdefghijklmnopqrstuvwxyzE'

carte = []

with open('test.txt', 'r') as fichier:
    lignes = fichier.readlines()
    for ligne in lignes:
        carte.append([])
        for hauteur in ligne[:-1]:
            if hauteur == 'S':
                dep_x = lignes.index(ligne) + 1
                dep_y = ligne.index('S') + 1
                carte[len(carte)-1].append(('a', True))

            elif hauteur == 'E':
                arr_x = lignes.index(ligne) + 1
                arr_y = ligne.index('E') + 1
                carte[len(carte)-1].append(('E', False))

            else:
                carte[len(carte)-1].append((hauteur, False))

for k in range(len(carte)):
    carte[k] = [('.', True)] + carte[k] + [('.', True)]
ajout_carte = [('.', True) for _ in range(len(carte[0]))]
carte = [ajout_carte] + carte + [ajout_carte]


print(f'Carte traitée')
print(f'Coordonnées du point de départ : {dep_x, dep_y}')
print(f"Coordonnées du point d'arrivée : {arr_x, arr_y}")
print(f'Exploration de la carte ...')


def exploration(x,y,map):
    nouv_map = map.copy()
    nouv_map[x][y][1] = True
    hauteur = nouv_map[x][y][0]
    for xi in [-1, 1]:
        for yi in [-1, 1]:
            hauteur_voisine = nouv_map[x + xi][y + yi][0]
            if hauteur_voisine == 'E':
                return # a completer
            else:
                if liste_hauteurs.index(hauteur) < liste_hauteurs.index(hauteur_voisine) and not nouv_map[x+xi][y+yi][1]:

                else:



# ------------------- Partie 2 ------------------- #
print(f'# ------------------- Partie 2 ------------------- #')
