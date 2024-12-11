# ADVENT-OF-CODE 2023
# Jour 17
# https://adventofcode.com/2023/day/17

# --- Day 17: Clumsy Crucible ---

lines = open('../inputs/17.txt', 'r').readlines()
map = [[int(x) for x in line.strip()] for line in lines]

L = len(map)
C = len(map[0])

x = 0
y = 0
pertes = 0

ens_pertes = dict()
positions = [(x, y, pertes)]

pertes_finales = dict()

while positions:
    for (x, y, pertes) in positions:
    # Enregistre les pertes
        ens_pertes[(x, y, pertes)] = pertes + map[y][x]
        for 

        if (x, y) == (C-1, L-1):
            pertes_finales[]


