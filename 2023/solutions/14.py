# ADVENT-OF-CODE 2023
# Jour 14
# https://adventofcode.com/2023/day/14

# --- Day 14: Parabolic Reflector Dish ---

lines = open('../inputs/14.txt', 'r').readlines()

map_base = []

for line in lines:
    line = line.strip()
    map_base.append(line)


def translater_matrice_nord(matrice):
    matrice_translate = []
    for x in range(len(matrice[0])):
        ligne = ""
        for line in matrice:
            ligne += line[x]
        matrice_translate.append(ligne)
    return matrice_translate


def translater_matrice_est(matrice):
    matrice_translate = []
    for line in matrice:
        matrice_translate.append(line[::-1])
    return matrice_translate


def translater_matrice_sud(matrice):
    matrice_translate = translater_matrice_nord(matrice)
    matrice_translate = translater_matrice_est(matrice_translate)
    return matrice_translate


def translater_matrice_ouest(matrice):
    return matrice


def tilt(line: str):
    if "O" not in line:
        return line

    if "#" not in line:
        return "O" * line.count("O") + "." * line.count(".")

    position_hash = []
    for i in range(len(line)):
        if line[i] == '#':
            position_hash.append(i)
    resultat = ""
    current = 0
    for index_hash in position_hash:
        nbr_O = line[current:index_hash].count("O")
        nbr_pts = line[current:index_hash].count(".")
        partie_tilt = "O" * nbr_O + "." * nbr_pts + '#'
        resultat += partie_tilt
        current = index_hash

    nbr_O = line[current:].count("O")
    partie_tilt = "O" * nbr_O + "." * (len(line) - 1 - current - nbr_O)
    resultat += partie_tilt
    return resultat


def tilt_matrice(matrice):
    matrice_res = []
    for ligne in matrice:
        ligne_res = tilt(ligne)
        matrice_res.append(ligne_res)
    return matrice_res


def resultat(matrice):
    res = 0
    for i, ligne in enumerate(matrice):
        res += ligne.count("O") * (len(matrice[0]) - i)
    return res


# Partie 1 :

map_travail = translater_matrice_nord(map_base)
map_travail = tilt_matrice(map_travail)
map_travail = translater_matrice_sud(map_travail)
res = resultat(map_travail)

print(f"Partie 1 : {res}")


# Partie 2 :

def cycle_nord(map):
    map_t = translater_matrice_nord(map)
    map_t = tilt_matrice(map_t)
    map_t = translater_matrice_nord(map_t)
    return map_t


def cycle_sud(map):
    map = translater_matrice_sud(map)
    map = tilt_matrice(map)
    map = translater_matrice_est(map)
    map = translater_matrice_nord(map)

    return map


def cycle_ouest(map):
    map = tilt_matrice(map)
    return map


def cycle_est(map):
    map = translater_matrice_est(map)
    map = tilt_matrice(map)
    map = translater_matrice_est(map)
    return map


def get_key(val, dico):
    for key, value in dico.items():
        if val == value:
            return key


nbr_cycles = 1000000000
index_cycles = 0

map = map_base

dico_maps = {}
index_repet = 0
while index_cycles < nbr_cycles and map not in dico_maps.values():
    dico_maps[index_cycles] = map
    map = cycle_nord(map)
    map = cycle_ouest(map)
    map = cycle_sud(map)
    map = cycle_est(map)
    index_cycles += 1

index_repet = get_key(map, dico_maps)
index_fin = (nbr_cycles - index_repet) % (index_cycles - index_repet)
map_fin = dico_maps[index_fin + index_repet]
res = resultat(map_fin)

print(f"Partie 2 : {res}")
