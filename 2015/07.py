# ADVENT-OF-CODE 2015
# Jour 7
# https://adventofcode.com/2015/day/7

# --- Day 7: Some Assembly Required ---

# Partie 1
liste = []
lines = open('07.txt', 'r').readlines()
instructions = []
dict_cables = {}
for line in lines:
    line = line.strip().split(" -> ")
    wire = line[1]
    consigne = line[0].split(" ")
    instructions.append((wire, consigne))
    dict_cables[wire] = []

def trouver_consigne(key):
    n = len(instructions)
    for i in range(n):
        if instructions[i][0] == key:
            return instructions[i][1]

def binaire(entier: int):
    rep_bin = [0 for _ in range(16)]
    for k in range(0,17):
        if entier // 2**(16-k) == 1:
            rep_bin[16-k] = 1
            entier = entier % 2**(16-k)
    return rep_bin

def suivre_consigne(key, consigne):
    if len(consigne) == 1 :
        if consigne[0].isdigit():
            dict_cables[key] = binaire(int(consigne[0]))
        else:
            dict_cables[key] = calculate_value(consigne[0])

    elif consigne[0] == "NOT":
        wire = consigne[1]
        wire_value = calculate_value(wire)
        for k in range(len(wire_value)):
            if wire_value[k] == 0:
                wire_value[k] = 1
            else:
                wire_value[k] = 0
        dict_cables[key] = wire_value

    elif consigne[1] == "AND":
        if consigne[0].isdigit():
            wire1_v = binaire(int(consigne[0]))
        else :
            wire1= consigne[0]
            wire1_v = calculate_value(wire1)
        if consigne[2].isdigit():
            wire2_v = binaire(int(consigne[2]))
        else :
            wire2 =consigne[2]
            wire2_v = calculate_value(wire2)
        wire_v = []
        for i in range(len(wire1_v)):
            wire_v.append(wire1_v[i] and wire2_v[i])
        dict_cables[key] = wire_v

    elif consigne[1] == "OR":
        if consigne[0].isdigit():
            wire1_v = binaire(int(consigne[0]))
        else:
            wire1 = consigne[0]
            wire1_v = calculate_value(wire1)
        if consigne[2].isdigit():
            wire2_v = binaire(int(consigne[2]))
        else:
            wire2 = consigne[2]
            wire2_v = calculate_value(wire2)
        wire_v = []
        for i in range(len(wire1_v)):
            wire_v.append(wire1_v[i] or wire2_v[i])
        dict_cables[key] = wire_v

    elif consigne[1] == "RSHIFT":
        wire = consigne[0]
        decalage = int(consigne[2])
        wire_value = calculate_value(wire)
        dict_cables[key] = wire_value[decalage:] + [0 for _ in range(decalage)]

    elif consigne[1] == "LSHIFT":
        wire = consigne[0]
        decalage = int(consigne[2])
        wire_value = calculate_value(wire)
        dict_cables[key] = [0 for _ in range(decalage)] + wire_value[:16-decalage]

def calculate_value(key):
    if dict_cables[key] != []:
        return dict_cables[key]
    else:
        consigne = trouver_consigne(key)

        suivre_consigne(key, consigne)
        return dict_cables[key]

def bin2dec(binaire):
    entier = 0
    for k in range(16):
        entier += binaire[16-k-1] * 2**(16-k-1)
    return entier

a = bin2dec(calculate_value("a"))
print(f"Partie 1 : {a}")

# Partie 2

for keys in dict_cables.keys():
    dict_cables[keys] = []
dict_cables["b"] = binaire(a)

a = bin2dec(calculate_value("a"))
print(f"Partie 2 : {a}")
