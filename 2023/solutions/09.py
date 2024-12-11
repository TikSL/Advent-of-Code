# ADVENT-OF-CODE 2023
# Jour 9
# https://adventofcode.com/2023/day/9

# --- Day 9: Mirage Maintenance ---

lines = open('../inputs/09.txt', 'r').readlines()

sequences = []

for line in lines:
    line = line.strip()
    seq = [[]]
    for x in line.split(" "):
        seq[0].append(int(x))
    sequences.append(seq)


def contient_unique_elt(liste):
    return len(set(liste)) == 1

def calculer_diff(liste:list):
    while not contient_unique_elt(liste[-1]):
        differences = []
        for i in range(1, len(liste[-1])):
            differences.append(liste[-1][i] - liste[-1][i-1])
        liste.append(differences)
    return liste

def trouver_prochain(sequence):
    sequence = calculer_diff(sequence)
    n = len(sequence)
    i = n-2
    while i >=0:
        sequence[i].append(sequence[i][-1] + sequence[i+1][-1])
        i-=1
    return sequence

somme = 0
for sequence in sequences:
    somme += trouver_prochain(sequence)[0][-1]

print(f"Partie 1 : {somme}")

# Partie 2

sequences = []

for line in lines:
    line = line.strip()
    seq = [[]]
    for x in line.split(" "):
        seq[0].append(int(x))
    sequences.append(seq)
def trouver_precedent(sequence):
    sequence = calculer_diff(sequence)
    n = len(sequence)
    i = n-2
    while i >=0:
        sequence[i] = [sequence[i][0] - sequence[i+1][0]] + sequence[i]
        i-=1
    return sequence

somme = 0
for sequence in sequences:
    somme += trouver_precedent(sequence)[0][0]

print(f"Partie 2 : {somme}")
