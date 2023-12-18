# ADVENT-OF-CODE 2023
# Jour 18
# https://adventofcode.com/2023/day/18

# --- Day 18: Lavaduct Lagoon ---

lines = open('18.txt', 'r').readlines()
lines = [x.strip().split(" ") for x in lines]
lines1 = [(x[0], int(x[1]), x[2]) for x in lines]


# Partie 1 :
pos = [(0,0)]

x, y = 0, 0

for (ordre, valeur, _) in lines1:
    if ordre == "R":
        x, y = x + valeur, y
    elif ordre == "L":
        x, y = x - valeur, y
    elif ordre == "D":
        x, y = x, y + valeur
    else: # ordre == "U"
        x, y = x, y - valeur
    pos.append((x,y))

aire = 0
for i, (x,y) in enumerate(pos[:-1]):
    aire += y * (pos[i-1][0] - pos[i+1][0])
aire += pos[len(pos)-1][1] *(pos[len(pos)-2][0] - pos[0][0])
aire //= 2

aire += sum([k for (_,k,_) in lines1])//2 + 1

print(f"Partie 1 : {aire}")

# Partie 2 :

lines2 = [(int(x[:-1][-1]), int(x[2:-1][:-1],16)) for (_,_,x) in lines]
pos = [(0,0)]
x, y = 0, 0

for ordre, valeur in lines2:
    if ordre == 0:
        x, y = x + valeur, y
    elif ordre == 2:
        x, y = x - valeur, y
    elif ordre == 1:
        x, y = x, y + valeur
    else:  # ordre == "U"
        x, y = x, y - valeur
    pos.append((x, y))

aire = 0
for i, (x, y) in enumerate(pos[:-1]):
    aire += y * (pos[i - 1][0] - pos[i + 1][0])
aire += pos[len(pos) - 1][1] * (pos[len(pos) - 2][0] - pos[0][0])
aire //= 2

aire += sum([k for (_, k) in lines2]) // 2 + 1

print(f"Partie 2 : {aire}")

