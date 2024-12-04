# ADVENT-OF-CODE 2024
# Jour 4
# https://adventofcode.com/2024/day/4
from enum import verify

# --- Day 4: Ceres Search ---

grid = []

with open('04.txt', 'r') as file:

    lines = file.readlines()
    for j, line in enumerate(lines):
        line = line.strip()
        grid.append(line)

NBR_COLUMNS = len(grid)
NBR_LINES = len(grid[0])

def check_left(l, c, grid):
    if c < 3:
        return 0
    if grid[l][c-1] == 'M' and grid[l][c-2] == 'A' and grid[l][c-3] == 'S':
        return 1
    return 0


def check_right(l, c, grid):
    if c > NBR_COLUMNS - 4:
        return 0
    if grid[l][c + 1] == 'M' and grid[l][c + 2] == 'A' and grid[l][c + 3] == 'S':
        return 1
    return 0


def check_up(l, c, grid):
    if l < 3:
        return 0
    if grid[l-1][c] == 'M' and grid[l-2][c] == 'A' and grid[l-3][c] == 'S':
        return 1
    return 0


def check_down(l, c, grid):
    if l > NBR_LINES - 4:
        return 0
    if grid[l + 1][c] == 'M' and grid[l + 2][c] == 'A' and grid[l + 3][c] == 'S':
        return 1
    return 0


def check_diag_right_up(l, c, grid):
    if l < 3 or c > NBR_COLUMNS - 4:
        return 0
    if grid[l - 1][c + 1] == 'M' and grid[l - 2][c + 2] == 'A' and grid[l - 3][c + 3] == 'S':
        return 1
    return 0


def check_diag_right_down(l, c, grid):
    if l > NBR_LINES - 4 or c > NBR_COLUMNS - 4:
        return 0
    if grid[l + 1][c + 1] == 'M' and grid[l + 2][c + 2] == 'A' and grid[l + 3][c + 3] == 'S':
        return 1
    return 0


def check_diag_left_up(l, c, grid):
    if l < 3 or c < 3:
        return 0
    if grid[l - 1][c - 1] == 'M' and grid[l - 2][c - 2] == 'A' and grid[l - 3][c - 3] == 'S':
        return 1
    return 0


def check_diag_left_down(l, c, grid):
    if l > NBR_LINES - 4 or c < 3:
        return 0
    if grid[l + 1][c - 1] == 'M' and grid[l + 2][c - 2] == 'A' and grid[l + 3][c - 3] == 'S':
        return 1
    return 0


def count_XMAS(l, c, grid):
    count = 0

    count += check_left(l, c, grid)
    count += check_right(l, c, grid)
    count += check_up(l, c, grid)
    count += check_down(l, c, grid)

    count += check_diag_right_up(l, c, grid)
    count += check_diag_right_down(l, c, grid)
    count += check_diag_left_up(l, c, grid)
    count += check_diag_left_down(l, c, grid)

    return count


def verify_X_MAS(l, c, grid):
    if l == 0 or l == NBR_LINES - 1:
        return 0
    if c == 0 or c == NBR_COLUMNS - 1:
        return 0
    if grid[l-1][c - 1] == 'M' and grid[l+1][c-1] == 'M' and grid[l-1][c+1] == 'S' and grid[l+1][c+1] == 'S':
        return 1
    if grid[l-1][c - 1] == 'S' and grid[l+1][c-1] == 'S' and grid[l-1][c+1] == 'M' and grid[l+1][c+1] == 'M':
        return 1
    if grid[l-1][c - 1] == 'S' and grid[l+1][c-1] == 'M' and grid[l-1][c+1] == 'S' and grid[l+1][c+1] == 'M':
        return 1
    if grid[l-1][c - 1] == 'M' and grid[l+1][c-1] == 'S' and grid[l-1][c+1] == 'M' and grid[l+1][c+1] == 'S':
        return 1
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
