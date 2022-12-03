# ADVENT-OF-CODE 2021
# Jour 03
# https://adventofcode.com/2021/day/3

print(f'# ------------------------------------------------ #')
print(f'#             Advent Of Code 2021 - 03             #')
print(f'#                 Binary Diagnostic                #')
print(f'# ------------------------------------------------ #\n')

# ------------------- Partie 1 ------------------- #
print(f'# ------------------- Partie 1 ------------------- #')

with open('03.txt', 'r') as fichier:
    lignes = fichier.readlines()
    n = len(lignes[0][:-1])  # nombre de bits
    liste_0 = [0 for k in range(n)]  # compte le nombre de 0 de chaque colonne
    for ligne in lignes:
        for k in range(n):
            liste_0[k] += int(ligne[k])

fichier.close()

gamma_bin = []
epsilon_bin = []

for k in range(n):
    if liste_0[k] < len(lignes)/2:
        gamma_bin.append(0)
        epsilon_bin.append(1)
    else:
        gamma_bin.append(1)
        epsilon_bin.append(0)

gamma = 0
epsilon = 0
for k in range(n):
    gamma += gamma_bin[k] * 2 ** (n - k - 1)
    epsilon += epsilon_bin[k] * 2 ** (n - k - 1)

print(f'Gamma binaire : {gamma_bin}, gamma : {gamma}\n'
      f'Epsilon binaire : {epsilon_bin}, epsilon : {epsilon}\n'
      f'Produit solution : {epsilon * gamma}')

# ------------------- Partie 2 ------------------- #
print(f'# ------------------- Partie 2 ------------------- #')


def plus_present_colonne(liste, colonne):
    somme = 0
    for binaire in liste:
        somme += int(binaire[colonne])
    if somme > len(liste)/2:  # 1 le plus présent
        return 1
    elif somme < len(liste)/2:
        return 0  # 0 le plus présent
    else:
        return 2  # égalité


liste_O2 = []
liste_CO2 = []
with open('03.txt', 'r') as fichier:
    lignes = fichier.readlines()
    for ligne in lignes:
        liste_O2.append(ligne[:-1])
        liste_CO2.append(ligne[:-1])
fichier.close()

indice_colonne = 0
while len(liste_O2) > 1:

    plus_present_O2 = plus_present_colonne(liste_O2, indice_colonne)

    nouvelle_liste_O2 = []

    if plus_present_O2 == 0:
        for nombre in liste_O2:
            if int(nombre[indice_colonne]) == 0:
                nouvelle_liste_O2.append(nombre)
        liste_O2 = nouvelle_liste_O2
    else:
        for nombre in liste_O2:
            if int(nombre[indice_colonne]) == 1:
                nouvelle_liste_O2.append(nombre)
        liste_O2 = nouvelle_liste_O2

    indice_colonne += 1

indice_colonne = 0
while len(liste_CO2) > 1:
    plus_present_CO2 = plus_present_colonne(liste_CO2, indice_colonne)

    nouvelle_liste_CO2 = []

    if plus_present_CO2 == 0:
        for nombre in liste_CO2:
            if int(nombre[indice_colonne]) == 1:
                nouvelle_liste_CO2.append(nombre)
        liste_CO2 = nouvelle_liste_CO2
    else:
        for nombre in liste_CO2:
            if int(nombre[indice_colonne]) == 0:
                nouvelle_liste_CO2.append(nombre)
        liste_CO2 = nouvelle_liste_CO2

    indice_colonne += 1

taux_O2 = 0
taux_CO2 = 0
for k in range(n):
    taux_O2 += int(liste_O2[0][k]) * 2 ** (n - k - 1)
    taux_CO2 += int(liste_CO2[0][k]) * 2 ** (n - k - 1)

print(f'Taux CO2 binaire : {liste_CO2[0]}, taux CO2 : {taux_CO2}\n'
      f'Taux 02 binaire : {liste_O2[0]}, taux O2 : {taux_O2}\n'
      f'Produit solution : {taux_CO2 * taux_O2}')
