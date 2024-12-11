# ADVENT-OF-CODE 2023
# Jour 16
# https://adventofcode.com/2023/day/16

# --- Day 16: The Floor Will Be Lava ---

lines = [line.strip() for line in open('../inputs/16.txt', 'r').readlines()]
map = [[x for x in line] for line in lines]

global cases_vues
global cases_vues_cpt

def score_energie(x_dep, y_dep, direction_depart):

    cases_vues = set()  # Coord + direction lumière
    cases_vues_cpt = set()

    cases_vues.add((x_dep, y_dep, direction_depart))
    cases_vues_cpt.add((x_dep, y_dep))

    position = [(x_dep, y_dep, direction_depart)]

    while position:

        for (x, y, direction) in position :
            if map[y][x] in '.\\/':
                if map[y][x] == '.':
                    direction_apres = direction
                elif map[y][x] == "/":
                    direction_apres = (-direction[1], -direction[0])
                else:
                    direction_apres = (direction[1], direction[0])
                x_apres = x + direction_apres[1]
                y_apres = y + direction_apres[0]
                if 0 <= x_apres < len(map[0]) and 0 <= y_apres < len(map) and (x_apres, y_apres, direction_apres) not in cases_vues:
                    cases_vues.add((x_apres, y_apres, direction_apres))
                    cases_vues_cpt.add((x_apres, y_apres))
                    position.append((x_apres, y_apres, direction_apres))
            else :
                if map[y][x] == "-":
                    if direction in [(0, 1), (0, -1)]:
                        direction_apres = direction
                        x_apres = x + direction_apres[1]
                        y_apres = y + direction_apres[0]
                        if 0 <= x_apres < len(map[0]) and 0 <= y_apres < len(map) and (
                        x_apres, y_apres, direction_apres) not in cases_vues:
                            cases_vues.add((x_apres, y_apres, direction_apres))
                            cases_vues_cpt.add((x_apres, y_apres))
                            position.append((x_apres, y_apres, direction_apres))

                    else:
                        directions_apres = [(0, 1), (0, -1)]
                        for direction_apres in directions_apres:
                            x_apres = x + direction_apres[1]
                            y_apres = y + direction_apres[0]
                            if 0 <= x_apres < len(map[0]) and 0 <= y_apres < len(map) and (
                            x_apres, y_apres, direction_apres) not in cases_vues:
                                cases_vues.add((x_apres, y_apres, direction_apres))
                                cases_vues_cpt.add((x_apres, y_apres))
                                position.append((x_apres, y_apres, direction_apres))

                else:  # Cas |

                    if direction in [(1, 0), (-1, 0)]:
                        direction_apres = direction
                        x_apres = x + direction_apres[1]
                        y_apres = y + direction_apres[0]
                        if 0 <= x_apres < len(map[0]) and 0 <= y_apres < len(map) and (
                        x_apres, y_apres, direction_apres) not in cases_vues:
                            cases_vues.add((x_apres, y_apres, direction_apres))
                            cases_vues_cpt.add((x_apres, y_apres))
                            position.append((x_apres, y_apres, direction_apres))
                    else:
                        directions_apres = [(1, 0), (-1, 0)]
                        for direction_apres in directions_apres:
                            x_apres = x + direction_apres[1]
                            y_apres = y + direction_apres[0]
                            if 0 <= x_apres < len(map[0]) and 0 <= y_apres < len(map) and (
                            x_apres, y_apres, direction_apres) not in cases_vues:
                                cases_vues.add((x_apres, y_apres, direction_apres))
                                cases_vues_cpt.add((x_apres, y_apres))
                                position.append((x_apres, y_apres, direction_apres))
            position.remove((x, y, direction))

    # for y in range(len(map)):
    #     for x in range(len(map[0])):
    #         if (x, y) in cases_vues_cpt:
    #             print("#", end="")
    #         else:
    #             print(".", end="")
    #     print("")

    return len(cases_vues_cpt)


print(f"Partie 1 : {score_energie(0,0, (0,1))}")

# Partie 2 :

maxi_energie = 0

for x in range(0, len(map[0])):
    energie_haut = score_energie(x, 0, (1, 0))
    energie_bas = score_energie(x, len(map) - 1, (-1, 0))
    maxi_energie = max(maxi_energie, energie_haut, energie_bas)

for y in range(0, len(map)):
    energie_gauche = score_energie(0, y, (0, 1))
    energie_droite = score_energie(len(map[0]) - 1,y,  (0, -1))
    maxi_energie = max(maxi_energie, energie_droite, energie_gauche)

print(f"Partie 2 : {maxi_energie}")
