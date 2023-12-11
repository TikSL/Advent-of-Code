# ADVENT-OF-CODE 2023
# Jour 10
# https://adventofcode.com/2023/day/10

# --- Day 10: Pipe Maze ---

lines = open('10.txt', 'r').readlines()

lines = ['.' + x.strip() + '.' for x in lines]
n = len(lines[0])
lines = ["."*n] + lines + ["."*n]

def simplifier_carte(carte):
    carte_simple = []
    y = 0
    for line in carte:
        x = 0
        ligne_carte = ""
        for caracter in line:
            if caracter == "-":
                if carte[y][x-1] in "L-FS" and carte[y][x+1] in "7-JS":
                    ligne_carte += "-"
                else :
                    ligne_carte += "."
            elif caracter == "|":
                if carte[y-1][x] in "F|7S" and carte[y+1][x] in "L|JS":
                    ligne_carte += "|"
                else :
                    ligne_carte += "."
            elif caracter == "L":
                if carte[y-1][x] in "F|7S" and carte[y][x+1] in "7-JS":
                    ligne_carte += "L"
                else:
                    ligne_carte += "."
            elif caracter == "7":
                if carte[y][x-1] in "L-FS" and carte[y+1][x] in "L|JS":
                    ligne_carte += "7"
                else:
                    ligne_carte += "."
            elif caracter == "F":
                if carte[y][x+1] in "7-JS" and carte[y+1][x] in "L|JS":
                    ligne_carte += "F"
                else:
                    ligne_carte += "."
            elif caracter == "J":
                if carte[y-1][x] in "F|7S" and carte[y][x-1] in "L-FS":
                    ligne_carte += "J"
                else:
                    ligne_carte += "."
            elif caracter == "S":
                ligne_carte += "S"
            else:
                ligne_carte += "."
            x += 1
        carte_simple.append(ligne_carte)
        y += 1
    return carte_simple

carte = lines
carte_simple = simplifier_carte(carte)

while carte_simple != carte:
    carte = carte_simple
    carte_simple = simplifier_carte(carte_simple)

for x in carte_simple:
    print(x)