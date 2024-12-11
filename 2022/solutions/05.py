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

with open('../inputs/05.txt', 'r') as fichier:
    lignes = fichier.readlines()

    caisses = [[] for k in range(nbr)]

    k = 0
    while lignes[k][:-1] != '':
        for i in range(len(lignes[k][:-1])):
            caract = lignes[k][:-1][i]
            if caract not in [' ',  '[', ']']:
                caisses[(i - 1) // 4].append(caract)
        k += 1

    for _ in range(nbr):
        caisses[_].pop()

    for ligne in lignes[k+1:len(lignes)]:
        instruction = ligne[:-1].split(' ')
        nombre = int(instruction[1])
        depart = int(instruction[3]) - 1
        arrivee = int(instruction[5]) - 1

        for _ in range(nombre):
            transfert = caisses[depart][0]
            caisses[depart].remove(transfert)
            caisses[arrivee] = list(transfert) + caisses[arrivee]

    print(f"Le haut des caisses donne : {''.join([caisses[k][0] for k in range(nbr)])}")

# ------------------- Partie 2 ------------------- #
print(f'# ------------------- Partie 2 ------------------- #')

nbr = 9

with open('../inputs/05.txt', 'r') as fichier:
    lignes = fichier.readlines()
    caisses = [[] for k in range(nbr)]
    k = 0
    while lignes[k][:-1] != '':
        for i in range(len(lignes[k][:-1])):
            caract = lignes[k][:-1][i]
            if caract not in [' ',  '[', ']']:
                caisses[(i - 1) // 4].append(caract)
        k += 1

    for _ in range(nbr):
        caisses[_].pop()

    for ligne in lignes[k+1:len(lignes)]:
        instruction = ligne[:-1].split(' ')
        nombre = int(instruction[1])
        depart = int(instruction[3]) - 1
        arrivee = int(instruction[5]) - 1

        transfert = caisses[depart][:nombre]
        caisses[depart] = caisses[depart][nombre:]
        caisses[arrivee] = transfert + caisses[arrivee]

    print(f"Le haut des caisses donne : {''.join([caisses[k][0] for k in range(nbr)])}")
