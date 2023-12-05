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

print(f"Partie 1 : {min(seeds)}")

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
            arr = dep + int(line[1:][i+1])
            liste = [k for k in range(dep, arr)]
            for k in liste:
                seeds.append(k)
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

seedsDepart = seeds

for etape in etapes:
    print(f"{etape=}")
    for i_seed in range(len(seeds)):
        seeds[i_seed] = destination(seeds[i_seed], maps[etape])
    print(f"{seeds=}")

for seed in seeds:
    if not(seed in seedsDepart):
        seeds.remove(seed)
print(f"{seeds=}")

print(f"Partie 2 : {min(seeds)}")