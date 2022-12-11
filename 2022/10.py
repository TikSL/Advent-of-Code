# ADVENT-OF-CODE 2022
# Jour 10
# https://adventofcode.com/2022/day/10

print(f'# ------------------------------------------------ #')
print(f'#             Advent Of Code 2022 - 10             #')
print(f'#                 Cathode-Ray Tube                 #')
print(f'# ------------------------------------------------ #\n')

# ------------------- Partie 1 ------------------- #
print(f'# ------------------- Partie 1 ------------------- #')

with open('10.txt', 'r') as fichier:
    lignes = fichier.readlines()
    valeurX = 1
    X = [1]
    for ligne in lignes:
        ordre = ligne[:-1].split(' ')
        if ordre[0] == 'noop':
            X.append(valeurX)
        else:
            valeur_incr = int(ordre[1])
            X.append(valeurX)
            valeurX += valeur_incr
            X.append(valeurX)

    forces_signaux = 0
    for x in [19, 59, 99, 139, 179, 219]:
        forces_signaux += (x+1) * X[x]

    print(forces_signaux)
# ------------------- Partie 2 ------------------- #
print(f'# ------------------- Partie 2 ------------------- #')

with open('10.txt', 'r') as fichier:
    lignes = fichier.readlines()
    valeurX = 1
    X = [1]
    ecran_tot=[]
    ecran = ''
    for ligne in lignes:
        if len(ecran) >= 40:
            ecran_tot.append(ecran)
            ecran = ''

        ordre = ligne[:-1].split(' ')

        if ordre[0] == 'noop':
            if len(ecran) in [valeurX-1, valeurX, valeurX+1]:
                ecran += '#'
            else:
                ecran += ' '
            X.append(valeurX)

        else:
            valeur_incr = int(ordre[1])
            if len(ecran) in [valeurX-1, valeurX, valeurX+1]:
                ecran += '#'
            else:
                ecran += ' '
            if len(ecran) >= 40:
                ecran_tot.append(ecran)
                ecran = ''
            X.append(valeurX)
            if len(ecran) in [valeurX-1, valeurX, valeurX+1]:
                ecran += '#'
            else:
                ecran += ' '
            valeurX += valeur_incr
            X.append(valeurX)


    ecran_tot.append(ecran)

    for ligne in ecran_tot:
        print(ligne)
