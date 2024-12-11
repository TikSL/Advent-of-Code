# ADVENT-OF-CODE 2022
# Jour 09
# https://adventofcode.com/2022/day/9

print(f'# ------------------------------------------------ #')
print(f'#             Advent Of Code 2022 - 09             #')
print(f'#                    Rope Bridge                   #')
print(f'# ------------------------------------------------ #\n')

# ------------------- Partie 1 ------------------- #
print(f'# ------------------- Partie 1 ------------------- #')


def distance (case1, case2):
    return max(abs(case2[0]-case1[0]), abs(case2[1]-case1[1]))

with open('../inputs/09.txt', 'r') as fichier:
    lignes = fichier.readlines()

    case_tete = (0, 0)
    case_queue = (0, 0)
    case_visitee = [case_queue]

    for ligne in lignes:

        ordre = ligne.split(' ')
        mouvement = ordre[0]
        pas = int(ordre[1])

        if mouvement == 'R':
            for _ in range(pas):
                ancienne_case_tete = case_tete
                case_tete = (case_tete[0]+1, case_tete[1])
                if distance(case_tete, case_queue) > 1:
                    case_queue = ancienne_case_tete
                case_visitee.append(case_queue)

        elif mouvement == 'L':
            for _ in range(pas):
                ancienne_case_tete = case_tete
                case_tete = (case_tete[0]-1, case_tete[1])
                if distance(case_tete, case_queue) > 1:
                    case_queue = ancienne_case_tete
                case_visitee.append(case_queue)

        elif mouvement == 'U':
            for _ in range(pas):
                ancienne_case_tete = case_tete
                case_tete = (case_tete[0], case_tete[1]+1)
                if distance(case_tete, case_queue) > 1:
                    case_queue = ancienne_case_tete
                case_visitee.append(case_queue)

        elif mouvement == 'D':
            for _ in range(pas):
                ancienne_case_tete = case_tete
                case_tete = (case_tete[0], case_tete[1] - 1)
                if distance(case_tete, case_queue) > 1:
                    case_queue = ancienne_case_tete
                case_visitee.append(case_queue)

    print(len(set(case_visitee)))

# ------------------- Partie 2 ------------------- #
print(f'# ------------------- Partie 2 ------------------- #')

case_visitee = [(0,0)]
with open('test.txt', 'r') as fichier:
    lignes = fichier.readlines()

    snake = [(0,0) for _ in range(10)]

    for ligne in lignes:

        ordre = ligne.split(' ')
        mouvement = ordre[0]
        pas = int(ordre[1])

        if mouvement == 'R':
            for _ in range(pas):
                snake_prec = snake.copy()
                snake[0] = (snake[0][0]+1, snake[0][1])
                if distance(snake[0], snake[1]) > 1:
                    snake = [snake[0]] + snake_prec[:-1]
                #print('R', snake)
                case_visitee.append(snake[9])

        elif mouvement == 'L':
            for _ in range(pas):
                snake_prec = snake.copy()
                snake[0] = (snake[0][0]-1, snake[0][1])
                if distance(snake[0], snake[1]) > 1:
                    snake = [snake[0]] + snake_prec[:-1]
                #print('L', snake)
                case_visitee.append(snake[9])

        elif mouvement == 'U':
            for _ in range(pas):
                snake_prec = snake.copy()
                snake[0] = (snake[0][0], snake[0][1]+1)
                if distance(snake[0], snake[1]) > 1:
                    snake = [snake[0]] + snake_prec[:-1]
                #print('U', snake)
                case_visitee.append(snake[9])

        elif mouvement == 'D':
            for _ in range(pas):
                snake_prec = snake.copy()
                snake[0] = (snake[0][0], snake[0][1]-1)
                if distance(snake[0], snake[1]) > 1:
                    snake = [snake[0]] + snake_prec[:-1]
                #print('D', snake)
                case_visitee.append(snake[9])

    print(len(set(case_visitee)))

    visitee = list(set(case_visitee))


    l1 = min(visitee)[0]
    l2 = max(visitee)[0]
    h1 = min(visitee)[1]
    h2 = max(visitee)[1]

    print(l1,l2,h1,h2)
    print(list(set(case_visitee)))

    grille_visu = [[' ' for _ in range(l2-l1)] for _ in range(h2-h1)]

    for x in range(-4,4):
        for y in range(-11,14):
            if (x,y) in case_visitee:
                grille_visu[x+4][y+11] = '#'

    for ligne in grille_visu:
        print(ligne)
