# ADVENT-OF-CODE 2023
# Jour 5
# https://adventofcode.com/2023/day/5

# --- Day 5: If You Give A Seed A Fertilizer ---

lines = open('05.txt', 'r').readlines()

maps = {}
seeds = []
etapes = []
etape = ""
for line in lines :
    line = line.strip()
    line = line.replace(':', "")

    line = line.split(" ")

    if line == [""]:
        pass


    elif line[0] == "seeds":

        for seed in line[1:]:
            seeds.append(int(seed))

    elif not(line[0].isdigit()):
        etape = line[0]
        maps[etape]= []
        etapes.append(etape)

    elif line[0].isdigit():
        liste_infos = []
        for info in line:
            liste_infos.append(int(info))


        maps[etape].append(liste_infos)
        maps[etape].sort(key=lambda tup: tup[1])


print(f"{etapes=}")

print(f"{seeds=}")

def destination(pt_depart:int, map:list):
    for consigne in map:
        sources_min = consigne[1]
        sources_max = consigne[1] + consigne[2]
        if pt_depart >= sources_min and pt_depart <= sources_max:
            ecart = pt_depart - consigne[1]
            return consigne[0] + ecart
    return pt_depart

for etape in etapes:
    print(f"{etape=}")
    for i_seed in range(len(seeds)):
        seeds[i_seed] = destination(seeds[i_seed], maps[etape])
    print(f"{seeds=}")

print(f"Partie 1 : {min(seeds)}\n\n")

# Partie 2:

maps = {}
seeds = []
etapes = []
etape = ""
for line in lines :
    line = line.strip()
    line = line.replace(':', "")

    line = line.split(" ")

    if line == [""]:
        pass

    elif line[0] == "seeds":
        i = 0
        while i < len(line[1:]):
            dep = int(line[1:][i])
            arr = dep + int(line[1:][i+1]) -1
            seeds.append((dep, arr))
            i += 2

    elif not(line[0].isdigit()):
        etape = line[0]
        maps[etape]= []
        etapes.append(etape)

    elif line[0].isdigit():
        liste_infos = []
        for info in line:
            liste_infos.append(int(info))
        maps[etape].append(liste_infos)
        maps[etape].sort(key=lambda tup: tup[1])


print(f"{etapes=}")

print(f"{seeds=}")

def destination2(dep:int, arr:int, map:list):
    rendu = dep
    liste_nouv = []
    while rendu < arr:
        n = len(map)
        for i in range(n):
            print(rendu, liste_nouv)
            consigne = map[i]
            ci_min = consigne[1]
            ci_max = consigne[1] + consigne[2]
            if rendu < ci_min: # on est avant la consigne
                if arr < ci_min: # on est avant la consigne ET si on est QUE avant
                    liste_nouv.append((rendu, arr))
                    return liste_nouv
                else: #on est avant la consigne ET si on est une partie avant => on découpe
                    liste_nouv.append((rendu, ci_min-1))
                    rendu = ci_min

            if rendu > ci_max: # si on est après la consigne
                if i == n - 1: # mais que c'était la dernière
                    liste_nouv.append((rendu, arr))
                    return liste_nouv
            else : # on commence dans la consigne
                if arr <= ci_max : # ET qu'on termine dans la consigne
                    liste_nouv.append((consigne[0]+ rendu - consigne[1],consigne[0] + arr - consigne[1]))
                    return liste_nouv
                else :
                    liste_nouv.append((consigne[0] + rendu - consigne[1], consigne[0] + consigne[2]- consigne[1]))
                    rendu = ci_max + 1

            i += 1
    return liste_nouv


seedsDepart = seeds

for etape in etapes:
    print(f"{etape=}")
    nouv_seeds = []
    for i_seed in range(len(seeds)):
        (debut, arr) = seeds[i_seed]
        nouv_seeds += destination2(debut,arr, maps[etape])
    seeds = nouv_seeds
    print(f"{nouv_seeds=}")


# for seed in seeds:
#     if not(seed in seedsDepart):
#         seeds.remove(seed)
# print(f"{seeds=}")

# print(f"Partie 2 : {min(seeds)}")