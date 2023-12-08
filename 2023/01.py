# ADVENT-OF-CODE 2023
# Jour 1
# https://adventofcode.com/2023/day/1

# --- Day 1: Trebuchet?! ---

sum_tot = 0
with open('01.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line[:-1]
        n = len(line) - 1

        i = 0
        while not line[i].isdigit():
            i += 1
        sum_tot += int(line[i]) * 10

        i = 0
        while not line[n-i].isdigit():
            i += 1
        sum_tot += int(line[n - i])

print(f'Partie 1 : {sum_tot}')

# Part 2
digit_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

nbr1 = None
i1 = None
nbr2 = None
i2 = None
somme = 0
with open('01.txt', 'r') as fichier:
    lignes = fichier.readlines()
    for ligne in lignes:
        texte = ligne[:-1]
        for i, carac in enumerate(texte) :
            if carac.isdigit():
                if not nbr1 :
                    nbr1 = int(carac)
                    nbr2 = int(carac)
                    i1 = i
                    i2 = i
                else:
                    nbr2 = int(carac)
                    i2 = i
        for mot in digit_list:
            if mot in texte:
                if i1 == None :
                    nbr1 = digit_list.index(mot) + 1
                    i1 = texte.index(mot)
                if i1 > texte.index(mot):
                    nbr1 = digit_list.index(mot) + 1
                    i1 = texte.index(mot)
                if not(i2) or i2 < texte.index(mot):
                    nbr2 = digit_list.index(mot) + 1
                    i2 = texte.index(mot)
        somme += nbr1 * 10 + nbr2
        nbr1 = None
        nbr2 = None
        i1, i2 = None, None


print(f'Partie 2 : {somme}')
