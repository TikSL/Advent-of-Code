# ADVENT-OF-CODE 2015
# Jour 1
# https://adventofcode.com/2015/day/1

# --- Day 1: Not Quite Lisp ---

# Partie 1

lines = open('../inputs/01.txt', 'r').readlines()

etage = 0
for caractere in lines[0]:
    if caractere == "(":
        etage += 1
    elif caractere ==")":
        etage -= 1

print(f'Partie 1 : {etage}')

# Partie 2

etage = 0
i = 0
while etage >= 0:
    if lines[0][i] == "(":
        etage += 1
    elif lines[0][i] ==")":
        etage -= 1
    i += 1

print(f'Partie 2 : {i}')
