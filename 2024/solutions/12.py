# ADVENT-OF-CODE 2024
# Jour 12
# https://adventofcode.com/2024/day/12

# --- Day 12: Garden Groups ---

map = []
with open("../inputs/12.txt") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        map.append([x for x in line])

seen = set()

c_max, l_max = len(map[0]), len(map)
sum = 0
sum2 = 0

for l, line in enumerate(map):
    for c, char in enumerate(line):
        aire = 0
        perimetre = 0
        cases_perim = {}

        liste_todo = [(l, c)]
        if (l, c) not in seen:
            while liste_todo:
                l2, c2 = liste_todo[0]
                liste_todo = liste_todo[1:]

                char2 = map[l2][c2]
                if (l2,c2) not in seen:
                    seen.add((l2,c2))
                    aire += 1
                    for i, (dl, dc) in enumerate([(-1, 0), (1, 0), (0, -1), (0, 1)]):
                        l_dl, c_dc = l2 + dl, c2 + dc

                        if 0 <= l_dl < l_max and 0 <= c_dc < c_max and char2 == map[l_dl][c_dc]:
                            liste_todo.append((l_dl, c_dc))

                        else:
                            if (dl, dc) not in cases_perim:
                                cases_perim[(dl, dc)] = set()

                            perimetre += 1
                            cases_perim[(dl, dc)].add((l2, c2))

            sum += aire * perimetre

        sides = 0

        for key, coord in cases_perim.items():
            seen_perim = set()
            for (lp, cp) in coord:
                if (lp, cp) not in seen_perim:
                    sides += 1
                    liste_todo = [(lp,cp)]
                    while liste_todo:
                        lp2, cp2 = liste_todo[0]
                        liste_todo = liste_todo[1:]

                        if (lp2,cp2) not in seen_perim:
                            seen_perim.add((lp2,cp2))
                            for dl, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                lp_dl, cp_dl = lp2 + dl, cp2 + dc
                                if (lp_dl, cp_dl) in coord:
                                    liste_todo.append((lp_dl, cp_dl))

        sum2 += aire * sides

print(f"Partie 1 : {sum}")
print(f"Partie 2 : {sum2}")
