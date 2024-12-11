# ADVENT-OF-CODE 2015
# Jour 9
# https://adventofcode.com/2015/day/9

# --- Day 9: All in a Single Night ---

# Partie 1
from itertools import permutations

lines = open('../inputs/09.txt', 'r').readlines()

distances = {}
lieux = []

for line in lines :
    line = line.strip()
    line = line.split(" = ")
    ville1 = line[0].split(" to ")[0]
    ville2 = line[0].split(" to ")[1]
    dist = int(line[1])

    distances[(ville1, ville2)] = dist
    distances[(ville2, ville1)] = dist
    lieux.append(ville1)
    lieux.append(ville2)

lieux = set(lieux)

distances_cumul = []

for trajet in permutations(lieux):
    distance_voyage = 0
    for i in range(1, len(trajet)):
        distance_voyage += distances[(trajet[i], trajet[i-1])]
    distances_cumul.append(distance_voyage)

print(min(distances_cumul))

# Partie 2
print(max(distances_cumul))
