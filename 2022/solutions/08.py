# ADVENT-OF-CODE 2022
# Jour 08
# https://adventofcode.com/2022/day/8

print(f'# ------------------------------------------------ #')
print(f'#             Advent Of Code 2022 - 08             #')
print(f'#                Treetop Tree House                #')
print(f'# ------------------------------------------------ #\n')

# ------------------- Partie 1 ------------------- #
print(f'# ------------------- Partie 1 ------------------- #')

with open('../inputs/08.txt', 'r') as fichier:
    lignes = fichier.readlines()
    n = len(lignes[0])
    grille_visible = [[0 for _ in range(n-1)] for _ in range(n-1)]
    foret = [[0 for _ in range(n-1)] for _ in range(n-1)]

    n = len(foret)
    for x in range(len(lignes)):
        ligne = lignes[x][:-1]
        for y in range(len(ligne)):
            foret[x][y] = int(lignes[x][y])

    i_ligne = 0
    for rangee in foret[:-1]:
        i_colonne = 0
        for arbre in rangee:

            if (i_ligne == 0 or i_ligne == n - 1) or (i_colonne == 0 or i_colonne ==n-1):
                grille_visible[i_ligne][i_colonne] = 1
            else:
                if arbre > max(rangee[:i_colonne]) or arbre > max(rangee[i_colonne + 1:]) or arbre > max([foret[k][i_colonne] for k in range(i_ligne)]) or arbre > max([foret[k][i_colonne] for k in range(i_ligne + 1, n)]):
                    grille_visible[i_ligne][i_colonne] = 1

            i_colonne += 1

        i_ligne += 1

    somme = 0
    for ligne in grille_visible:
        somme += sum(ligne)

    print(somme + n)

# ------------------- Partie 2 ------------------- #
print(f'# ------------------- Partie 2 ------------------- #')


def vue_arbre(h_arbre, liste):
    n = len(liste)
    for k in range(n):
        if liste[k] >= h_arbre:
            return k + 1
    return n


with open('../inputs/08.txt', 'r') as fichier:
    lignes = fichier.readlines()
    n = len(lignes[0])
    grille_visible = [[0 for _ in range(n-1)] for _ in range(n-1)]
    foret = [[0 for _ in range(n-1)] for _ in range(n-1)]

    n = len(foret)
    for x in range(len(lignes)):
        ligne = lignes[x][:-1]
        for y in range(len(ligne)):
            foret[x][y] = int(lignes[x][y])

    score_vue = 0
    i_ligne = 0
    for rangee in foret[:-1]:
        i_colonne = 0
        for arbre in rangee:

            liste_gauche = [foret[i_ligne][y] for y in range(0, i_colonne)]
            liste_droite = [foret[i_ligne][y] for y in range(i_colonne+1, n)]

            liste_haut = [foret[x][i_colonne] for x in range(0, i_ligne)]
            liste_bas = [foret[x][i_colonne] for x in range(i_ligne+1, n)]

            liste_gauche.reverse()
            liste_haut.reverse()


            print(arbre)
            print(liste_haut, liste_gauche, liste_droite, liste_bas)
            print(vue_arbre(arbre, liste_gauche),  vue_arbre(arbre, liste_droite) ,vue_arbre(arbre, liste_bas), vue_arbre(arbre, liste_haut) )
            score_arbre = vue_arbre(arbre, liste_gauche) * vue_arbre(arbre, liste_droite) * vue_arbre(arbre, liste_bas) * vue_arbre(arbre, liste_haut)
            print(score_arbre)

            if score_arbre > score_vue:
                score_vue = score_arbre

            i_colonne += 1

        i_ligne += 1

    print(score_vue)
