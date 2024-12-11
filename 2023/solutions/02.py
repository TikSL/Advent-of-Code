# ADVENT-OF-CODE 2023
# Jour 2
# https://adventofcode.com/2023/day/2

# --- Day 2: Cube Conundrum ---

lines = open('../inputs/02.txt', 'r').readlines()
games = []
for line in lines:
    game = line.split(":")[1]
    game = game.replace("\n", "")
    game = game.replace(" ", "")
    game = game.replace("red", "r")
    game = game.replace("green", "g")
    game = game.replace("blue", "b")
    games.append(game)


# Partie 1

somme = 0

for i, game in enumerate(games):

    tirages = game.split(";")
    game_valide = True
    for tirage in tirages:
        cubes_tirage = tirage.split(",")
        for cube in cubes_tirage:
            if cube[-1] == 'r' and int(cube[:-1]) > 12:
                game_valide = False
            elif cube[-1] == 'g' and int(cube[:-1]) > 13:
                game_valide = False
            elif cube[-1] == 'b' and int(cube[:-1]) > 14:
                game_valide = False
    if game_valide:
        somme += i + 1

print(f'Partie 1 : {somme}')

# Partie 2

somme = 0

for i, game in enumerate(games):

    tirages = game.split(";")
    r, g, b = 0, 0, 0
    for tirage in tirages:
        cubes_tirage = tirage.split(",")
        for cube in cubes_tirage:
            if cube[-1] == 'r':
                r = max(r, int(cube[:-1]))
            elif cube[-1] == 'g':
                g = max(g, int(cube[:-1]))
            elif cube[-1] == 'b':
                b = max(b, int(cube[:-1]))
    somme += r*g*b

print(f'Partie 2 : {somme}')
