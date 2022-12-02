# ADVENT-OF-CODE 2022
# Jour 2
# https://adventofcode.com/2022/day/2

# ------------------- Tâche 1 ------------------- #
actions_adversaire = ['A', 'B', 'C']  # Pierre, Feuille, Ciseaux
actions_joueur = ['X', 'Y', 'Z']  # Pierre, Feuille, Ciseaux

score = 0

with open('02.txt', 'r') as fichier:
    lignes = fichier.readlines()
    for ligne in lignes:
        adversaire = actions_adversaire.index(ligne[0])
        joueur = actions_joueur.index(ligne[2])
        score += joueur + 1
        if joueur == adversaire:
            score += 3
        elif joueur == (adversaire + 1) % 3:
            score += 6
        else:
            score += 0

fichier.close()
print(f'Vous avez obtenu {score} points !')

# ------------------- Tâche 2 ------------------- #
