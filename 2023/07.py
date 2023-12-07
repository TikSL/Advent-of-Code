# ADVENT-OF-CODE 2023
# Jour 7
# https://adventofcode.com/2023/day/7

# --- Day 7: Camel Cards ---

lines = open('07.txt', 'r').readlines()

mains_a_classer = []
for line in lines:
    line = line.strip()
    main, bet = line.split(" ")
    mains_a_classer.append(([k for k in main], int(bet)))

valeurs = "AKQJT98765432"


def score(main):
    cartes_diff = set(main)
    nbr_cartes_diff = len(cartes_diff)
    if nbr_cartes_diff == 1:
        return 7
    elif nbr_cartes_diff == 2:
        maximum = max([main.count(k) for k in cartes_diff])
        if maximum == 4:
            return 6
        else:
            return 5
    elif nbr_cartes_diff == 3:
        maximum = max([main.count(k) for k in cartes_diff])
        if maximum == 3:
            return 4
        else:
            return 3
    elif nbr_cartes_diff == 4:
        return 2
    else:
        return 1


def estMeilleure(main1, main2):
    # Vérifie que main1 est meilleure que main2
    score_main1 = score(main1)
    score_main2 = score(main2)
    if score_main1 != score_main2:
        return score_main1 > score_main2
    else:
        i = 0
        while main1[i] == main2[i]:
            i += 1
        return valeurs.index(main1[i]) < valeurs.index(main2[i])


def classer(liste_classee, main, bet):
    i = 0
    while i < len(liste_classee):
        if estMeilleure(liste_classee[i][0], main):
            liste_classee = liste_classee[:i] + [(main, bet)] + liste_classee[i:]
            return liste_classee
        i += 1
    return liste_classee + [(main, bet)]


mains_classees = []
for i in range(len(mains_a_classer)):
    mains_classees = classer(mains_classees, mains_a_classer[i][0], mains_a_classer[i][1])

resultat = 0
for i in range(len(mains_classees)):
    resultat += (i + 1) * mains_classees[i][1]
print(f"Partie 1 : {resultat}")

# Partie 2

valeurs = "AKQT98765432J"

def score(main):
    cartes_diff = set(main)
    if main == ['J', 'J','J', 'J','J']:
        return 7
    if "J" in cartes_diff:
        cartes_diff.remove("J")
        nbr_cartes_diff = len(cartes_diff)
        if nbr_cartes_diff == 1:
            return 7
        elif nbr_cartes_diff == 2:
            if main.count("J") == 3 or main.count("J") == 2:
                return 6
            else:
                maximum = max([main.count(k) for k in cartes_diff])
                if maximum == 3:
                    return 6
                else:
                    return 5
        elif nbr_cartes_diff == 3:
            return 4
        else:
            return 2

    else:
        nbr_cartes_diff = len(cartes_diff)
        if nbr_cartes_diff == 1:
            return 7
        elif nbr_cartes_diff == 2:
            maximum = max([main.count(k) for k in cartes_diff])
            if maximum == 4:
                return 6
            else:
                return 5
        elif nbr_cartes_diff == 3:
            maximum = max([main.count(k) for k in cartes_diff])
            if maximum == 3:
                return 4
            else:
                return 3
        elif nbr_cartes_diff == 4:
            return 2
        else:
            return 1

mains_classees = []
for i in range(len(mains_a_classer)):
    mains_classees = classer(mains_classees, mains_a_classer[i][0], mains_a_classer[i][1])

resultat = 0
for i in range(len(mains_classees)):
    resultat += (i + 1) * mains_classees[i][1]
print(f"Partie 2 : {resultat}")