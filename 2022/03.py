# ADVENT-OF-CODE 2022
# Jour 03
# https://adventofcode.com/2022/day/3


print(f'# ------------------------------------------------ #')
print(f'#             Advent Of Code 2022 - 03             #')
print(f'#           Réorganisation des sacs à dos          #')
print(f'# ------------------------------------------------ #\n')

# ------------------- Partie 1 ------------------- #
print(f'# ------------------- Partie 1 ------------------- #')

prio = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def lettre_commune(mot1, mot2):
    for x in mot1:
        if x in mot2:
            return x


somme_prio = 0

with open('03.txt', 'r') as fichier:
    lignes = fichier.readlines()
    for ligne in lignes:
        texte = ligne[:-1]
        n = len(texte)//2
        item1, item2 = texte[:n], texte[n:]
        lettre = lettre_commune(item1, item2)

        somme_prio += prio.index(lettre) + 1

fichier.close()
print(f'Somme des priorités : {somme_prio}.')

# ------------------- Partie 2 ------------------- #
print(f'# ------------------- Partie 2 ------------------- #')


def lettre_commune_groupe(mot1, mot2, mot3):
    for x in mot1:
        if x in mot2 and x in mot3:
            return x


somme_prio = 0
with open('03.txt', 'r') as fichier:
    lignes = fichier.readlines()
    mots_groupe = []
    n = len(lignes)
    compteur = 0
    for k in range(n):
        mot = lignes[k][:-1]
        mots_groupe.append(mot)
        compteur += 1
        if compteur == 3:
            lettre = lettre_commune_groupe(mots_groupe[0], mots_groupe[1], mots_groupe[2])
            somme_prio += prio.index(lettre) + 1
            mots_groupe = []
            compteur = 0


fichier.close()
print(f'Somme des nouvelles priorités : {somme_prio}.')
