# ADVENT-OF-CODE 2024
# Jour 11
# https://adventofcode.com/2024/day/11

# --- Day 11: Plutonian Pebbles---

stones = open("input/11.txt").readlines()[0]
stones = [int(x) for x in stones.split()]

DicoValueDeep = {}

def solve(value, deep):
    if (value,deep) in DicoValueDeep:
        return DicoValueDeep[(value,deep)]
    if deep==0:
        ret = 1
    elif value==0:
        ret = solve(1, deep-1)
    elif len(str(value))%2==0:
        str1 = str(value)
        left = str1[:len(str1)//2]
        right = str1[len(str1)//2:]
        left, right = (int(left), int(right))
        ret = solve(left, deep-1) + solve(right, deep-1)
    else:
        ret = solve(value*2024, deep-1)
    DicoValueDeep[(value,deep)] = ret
    return ret

def solve_all(t):
    return sum(solve(x, t) for x in stones)

print(f"Partie 1 : {solve_all(25)}")
print(f"Partie 2 : {solve_all(75)}")
