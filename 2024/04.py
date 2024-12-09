# ADVENT-OF-CODE 2024
# Jour 4
# https://adventofcode.com/2024/day/4

# --- Day 4: Ceres Search ---

grid = []

with open('input/04.txt', 'r') as file:

    lines = file.readlines()
    for j, line in enumerate(lines):
        line = line.strip()
        grid.append(line)

NBR_COLUMNS = len(grid)
NBR_LINES = len(grid[0])

def check_xmas(l,c, dl, dc, grid):
    res = 0
    try :
        if (grid[l + 1 * dl][c + 1 * dc] == 'M'
                and grid[l + 2 * dl][c + 2 * dc] == 'A'
                and grid[l + 3 * dl][c + 3 * dc] == 'S'
                and l + 1 * dl >= 0
                and l + 2 * dl >= 0
                and l + 3 * dl >= 0
                and c + 1 * dc >= 0
                and c + 2 * dc >= 0
                and c + 3 * dc >= 0):
            res = 1
    except IndexError:
        res = 0
    return res

def count_XMAS(l, c, grid):
    count = 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    for dl, dc in directions:
        count += check_xmas(l, c, dl, dc, grid)
    return count

def check_pattern(l, c, grid, pattern):
    return (grid[l - 1][c - 1] == pattern[0]
            and grid[l + 1][c - 1] == pattern[1]
            and grid[l - 1][c + 1] == pattern[2]
            and grid[l + 1][c + 1] == pattern[3]
            and l - 1 >= 0
            and c - 1 >= 0)

def verify_X_MAS(l, c, grid):

    patterns = [('M', 'M', 'S', 'S'),
                ('S', 'S', 'M', 'M',),
                ('S', 'M', 'S', 'M'),
                ('M', 'S', 'M', 'S')]

    for pattern in patterns:
        try :
            if check_pattern(l, c, grid, pattern):
                return 1
        except IndexError:
            pass
    return 0

nbr_XMAS = 0
nbr_X_MAS = 0

for l, line in enumerate(grid):

    for c, char in enumerate(line):
        if char == 'X':
           nbr_XMAS += count_XMAS(l, c, grid)
        if char == 'A':
            nbr_X_MAS += verify_X_MAS(l, c, grid)

print(f'Partie 1 : {nbr_XMAS}')
print(f'Partie 2 : {nbr_X_MAS}')