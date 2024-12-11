# ADVENT-OF-CODE 2023
# Jour 12
# https://adventofcode.com/2023/day/12

# --- Day 12: Hot Springs ---

lines = open('../inputs/12.txt', 'r').readlines()
lines = [x.strip() for x in lines]

rows = []

for line in lines:
    spring, sizes = line.split(' ')
    list_sizes = [int(sizes.split(',')[0]), int(sizes.split(',')[1])]
    rows.append([spring, list_sizes])

# Partie 1

def verifier(schema, tailles):

    # 1. Faire une liste similaire à taille en recensant les #
    # 2. Parcourir cette liste et comparer à tailles

    n = len(schema)
    i = 0
    tailles_reelles = []
    compteur = 0
    while i < n and schema[i] != "?":
        if schema[i] == '#':
            compteur += 1
        if schema[i] == ".":
            if compteur != 0:
                tailles_reelles.append(compteur)
            compteur = 0
        i += 1

    if len(tailles_reelles) > len(tailles):
        return False

    for i in range(len(tailles_reelles)):
        if tailles_reelles[i] != tailles[i]:
            return False
    return True



def generer(schema_a_completer, tailles):
    liste_schemas_valides = [schema_a_completer]

    for schema in liste_schemas_valides:
        n = len(schema)
        for i in range(n) :
            print(schema[i])
            if schema[i] == "?":
                schemas_possib = [schema[:i] + "." + schema[i+1:] , schema[:i] + "#" + schema[i+1:]]
                schemas_possib_OK =[]
                for schema_a_test in schemas_possib:
                    if verifier(schema_a_test, tailles):
                        schemas_possib_OK.append(schema_a_test)
                liste_schemas_valides = schemas_possib_OK
    print(liste_schemas_valides)
    return liste_schemas_valides


def generation_totale(schema, tailles):
    liste_schemas_valides = [schema]
    liste_index_interro = []
    for i, k in enumerate(liste_schemas_valides):
        if "?" in k :
            print(k)
            liste_index_interro.append(i)

    while len(liste_index_interro) > 0:
        print(liste_index_interro)

        nouvelles_liste = []
        a_suppr = []
        for i in liste_index_interro:
            liste_generee_i = generer(liste_schemas_valides[i], tailles)
            nouvelles_liste.append(liste_generee_i)
            a_suppr.append(liste_schemas_valides[i])
        for x in a_suppr:
            liste_schemas_valides.remove(x)
        liste_schemas_valides += nouvelles_liste
        liste_index_interro = []
        for i, k in enumerate(liste_schemas_valides):
            if "?" in k:
                liste_index_interro.append(k)
    return liste_schemas_valides


print(generation_totale('???.###', [1,1,3]))
print("?" in '??..###')
# somme = 0
# for schema, tailles in rows:
#     possibilites = generer(schema, tailles)
#     print(possibilites)
#     n = len(possibilites)
#     somme += n
#
# print(f"Partie 1 : {somme}")


