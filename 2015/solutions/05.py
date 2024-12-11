# ADVENT-OF-CODE 2015
# Jour 5
# https://adventofcode.com/2015/day/5

# --- Day 5: Doesn't He Have Intern-Elves For This? ---

# Partie 1

compteur_nice = 0

lines = open('../inputs/05.txt', 'r').readlines()


def trois_voyelles(line):
    compteur = 0
    for lettre in line:
        if lettre in "aeuio":
            compteur += 1
            if compteur == 3:
                return True
    return False


def repetition(line):
    for i in range(1, len(line)):
        if line[i] == line[i-1]:
            return True
    return False


def combi_interdite(line):
    return "ab" in line or "cd" in line or "pq" in line or "xy" in line


for line in lines:
    line = line.replace("\n","")
    if trois_voyelles(line) and repetition(line) and not combi_interdite(line):
        compteur_nice += 1

print(f"Partie 1 : {compteur_nice}")

# Partie 2


def repetition_part2_entre(line):
    for i in range(2, len(line)):
        if line[i] == line[i-2]:
            return True
    return False


def repetition_part2(line):
    for i in range(1, len(line)-2):
        # print(line, line[i-1] +  line[i],line[i+1:])
        if line[i-1] +  line[i] in line[i+1:]:
            return True
    return False


compteur_nice = 0
for line in lines:
    line = line.replace("\n", "")
    if repetition_part2_entre(line) and repetition_part2(line):
        compteur_nice +=1

print(f"Partie 2 : {compteur_nice}")
