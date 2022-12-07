# ADVENT-OF-CODE 2022
# Jour 07
# https://adventofcode.com/2022/day/7

print(f'# ------------------------------------------------ #')
print(f'#             Advent Of Code 2022 - 07             #')
print(f'#              No Space Left On Device             #')
print(f'# ------------------------------------------------ #\n')


def affichage(repo, compteur):
    print(" " * (compteur-1) * 5 + '- ' + repo['nom'])
    if repo['liste_fichier']:
        for k in repo['liste_fichier']:
            texte = " " * compteur * 5
            texte += "- " + str(k[1]) + ' , ' + str(k[0])
            print(texte)
            texte = ""
    compteur += 1
    for indice_sous_repo in repo.keys():
        if repo[indice_sous_repo] not in [repo['nom'], repo['liste_fichier']]:
            affichage(repo[indice_sous_repo], compteur)


# ------------------- Partie 1 ------------------- #
print(f'# ------------------- Partie 1 ------------------- #')

with open('07.txt', 'r') as fichier:
    lignes = fichier.readlines()

    arbre = {'nom': '/', 'liste_fichier': []}  # repertoire racine /

    dossier_courant = arbre

    pile = [arbre]

    for ligne in lignes[1:]:
        instruction = ligne[:-1].split(' ')

        # Si c'est une commande
        if instruction[0] == '$':
            commande = instruction[1]
            if commande == 'cd':
                cible = instruction[2]
                if cible == '..':
                    dossier_courant = pile.pop()
                else:
                    pile.append(dossier_courant)
                    dossier_courant = dossier_courant[cible]

        # Nouveau repertoire
        elif instruction[0] == 'dir':
            nom = instruction[1]
            dossier_courant[nom] = {'nom': nom, 'liste_fichier': []}

        # Nouveau fichier
        else:
            taille = int(instruction[0])
            nom = instruction[1]
            dossier_courant['liste_fichier'].append((taille, nom))


def taille_repo(repo):
    somme = 0

    for file in repo['liste_fichier']:
        somme += file[0]

    for indice_sous_repo in repo.keys():
        if repo[indice_sous_repo] not in [repo['nom'], repo['liste_fichier']]:
            somme += taille_repo(repo[indice_sous_repo])
    return somme


liste_inf_100000 = []


def affichage_taille(repo):
    for clefs in repo.keys():
        if clefs not in ['nom', 'liste_fichier']:
            t = taille_repo(repo[clefs])
            if t <= 100000:
                liste_inf_100000.append(t)
            affichage_taille(repo[clefs])


affichage_taille(arbre)

print(sum(liste_inf_100000))

# ------------------- Partie 2 ------------------- #
print(f'# ------------------- Partie 2 ------------------- #')

liste_t = [taille_repo(arbre)]


def remplir_liste_t(repo):
    for clefs in repo.keys():
        if clefs not in ['nom', 'liste_fichier']:
            t = taille_repo(repo[clefs])
            liste_t.append(t)
            remplir_liste_t(repo[clefs])


remplir_liste_t(arbre)
liste_t.sort(reverse=True)

taille_a_atteindre = 30000000 - (70000000 - liste_t[0])

prec = liste_t[0]
print(liste_t)
for t in liste_t[1:]:
    if t < taille_a_atteindre:
        print(prec)
        break
    else:
        prec = t