# ADVENT-OF-CODE 2022
# Jour 05
# https://adventofcode.com/2022/day/5

print(f'# ------------------------------------------------ #')
print(f'#             Advent Of Code 2022 - 05             #')
print(f'#                   Supply Stacks                  #')
print(f'# ------------------------------------------------ #\n')

# ------------------- Partie 1 ------------------- #
print(f'# ------------------- Partie 1 ------------------- #')

nbr = 9

with open('05.txt', 'r') as fichier:
    lignes = fichier.readlines()
    liste = [[] for k in range(nbr)]
    k = 0
    while lignes[k][:-1] != '':
        for i in range(len(lignes[k][:-1])):
            caract = lignes[k][:-1][i]
            if caract not in [' ',  '[', ']']:
                liste[(i-1)//4].append(caract)
        k += 1

    for _ in range(nbr):
        liste[_].pop()

    for ligne in lignes[k+1:len(lignes)]:
        instruction = ligne[:-1].split(' ')
        nombre = int(instruction[1])
        depart = int(instruction[3]) - 1
        arrivee = int(instruction[5]) - 1

        for _ in range(nombre):
            transfert = liste[depart][0]
            liste[depart].remove(transfert)
            liste[arrivee] = list(transfert) + liste[arrivee]

    affichage = ''
    for k in range(nbr):
        affichage += liste[k][0]

    print(affichage)

# ------------------- Partie 2 ------------------- #
print(f'# ------------------- Partie 2 ------------------- #')

nbr = 9

with open('05.txt', 'r') as fichier:
    lignes = fichier.readlines()
    liste = [[] for k in range(nbr)]
    k = 0
    while lignes[k][:-1] != '':
        for i in range(len(lignes[k][:-1])):
            caract = lignes[k][:-1][i]
            if caract not in [' ',  '[', ']']:
                liste[(i-1)//4].append(caract)
        k += 1

    for _ in range(nbr):
        liste[_].pop()
    print(liste)

    for ligne in lignes[k+1:len(lignes)]:
        instruction = ligne[:-1].split(' ')
        nombre = int(instruction[1])
        depart = int(instruction[3]) - 1
        arrivee = int(instruction[5]) - 1

        transfert = liste[depart][:nombre]
        print(instruction)
        print('yo', transfert)
        liste[depart] = liste[depart][nombre:]
        liste[arrivee] = transfert + liste[arrivee]
        print(liste)
    affichage = ''
    for k in range(nbr):
        affichage += liste[k][0]

    print(affichage)
