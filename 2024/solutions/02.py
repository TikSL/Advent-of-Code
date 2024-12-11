# ADVENT-OF-CODE 2024
# Jour 2
# https://adventofcode.com/2024/day/2

# --- Day 2: Red-Nosed Reports ---


def is_safe(list):
    if list != sorted(list) and list != sorted(list, reverse=True):
        return False
    for i in range(1, len(list)):
        if 0 == abs(list[i] - list[i - 1]) or abs(list[i] - list[i - 1]) > 3:
            return False
    return True


def is_dampener_safe(list):
    if is_safe(list):
        return True
    else :
        for i in range(1, len(list)+1):
            if is_safe(list[:i - 1] + list[i:]):
                return True
    return False


with open('../inputs/02.txt', 'r') as file:
    lines = file.readlines()
    cpt_1 = 0
    cpt_2 = 0
    for line in lines:
        line = line[:-1]
        line = line.split(" ")

        line = [int(x) for x in line]

        if is_safe(line):
            cpt_1 += 1
        if is_dampener_safe(line):
            cpt_2 += 1

    print("Partie 1 : ",cpt_1)
    print("Partie 2 : ",cpt_2)
