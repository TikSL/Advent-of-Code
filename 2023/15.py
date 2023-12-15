# ADVENT-OF-CODE 2023
# Jour 15
# https://adventofcode.com/2023/day/15

# --- Day 15: Lens Library ---

line = open('15.txt', 'r').readlines()[0].strip()
sequence = line.split(",")

def hash(step:str):
    resultat_hash = 0
    for x in step:
        ascii_code = ord(x)
        resultat_hash += ascii_code
        resultat_hash *= 17
        resultat_hash %= 256
    return resultat_hash

somme_resultats_hash = 0
for step in sequence:
    somme_resultats_hash += hash(step)

print(f"Partie 1 : {somme_resultats_hash}")

# Partie 2:

box = [[] for k in range(256)]

def codes(boite):
    codes = []
    for lentille in boite:
        codes.append(lentille[0])
    return codes

for step in sequence:
    if "=" in step:
        decomp_step = step.split("=")
        label = decomp_step[0]
        focal_length = int(decomp_step[1])
        id_box = hash(label)
        if label not in codes(box[id_box]):
            box[id_box].append([label, focal_length])
        else :
            id_label = [i for i, lentille in enumerate(box[id_box]) if lentille[0] == label][0]
            box[id_box][id_label] = [label, focal_length]
    elif "-" in step :
        decomp_step = step.split("-")
        label = decomp_step[0]
        id_box = hash(label)
        liste_id_label = [i for i, lentille in enumerate(box[id_box]) if lentille[0] == label]
        if len(liste_id_label) == 1:
            box[id_box].remove(box[id_box][liste_id_label[0]])

somme = 0
for i, boite in enumerate(box) :
    focusing_power_boite = 0
    for j, lentille in enumerate(boite):
        focusing_power_boite += (i+1) * (j+1) * lentille[1]
    somme += focusing_power_boite

print(f"Partie 2 : {somme}")
