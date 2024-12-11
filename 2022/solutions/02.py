# ADVENT-OF-CODE 2022
# Jour 2
# https://adventofcode.com/2022/day/2

print(f'# ------------------------------------------------ #')
print(f'#             Advent Of Code 2022 - 02             #')
print(f'#             Pierre, Feuille, Ciseaux             #')
print(f'# ------------------------------------------------ #\n')


actions_adversaire = ['A', 'B', 'C']  # Pierre, Feuille, Ciseaux
actions_joueur = ['X', 'Y', 'Z']  # Pierre, Feuille, Ciseaux


# ------------------- Partie 1 ------------------- #
print(f'# ------------------- Partie 1 ------------------- #')

score = 0

with open('../inputs/02.txt', 'r') as fichier:
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

print(f'Vous avez obtenu {score} points.')

# ------------------- Partie 2 ------------------- #
print(f'# ------------------- Partie 2 ------------------- #')

score = 0

with open('../inputs/02.txt', 'r') as fichier:
    lignes = fichier.readlines()
    for ligne in lignes:

        adversaire = actions_adversaire.index(ligne[0])
        choix = actions_joueur.index(ligne[2])

        if choix == 0:  # défaite
            joueur = (adversaire - 1) % 3
        elif choix == 2:  # victoire
            joueur = (adversaire + 1) % 3
        else:  # égalité
            joueur = adversaire
        score += joueur + 1 + 3 * choix

fichier.close()

print(f'Vous avez obtenu {score} points.')
