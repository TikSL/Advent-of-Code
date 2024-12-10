# ADVENT-OF-CODE 2024
# Jour 10
# https://adventofcode.com/2024/day/10

# --- Day 10: Hoof It ---

map = []
with open("input/10.txt") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        map.append([int(k) for k in line])

def score(map, y, x, summits):
    ret = 0
    ret_2 = 0
    for dir in [(1,0), (-1,0), (0,1), (0,-1)]:
        if 0 <= y + dir[0] < len(map) and 0 <= x + dir[1] < len(map[0]):
            if map[y][x]==8 and map[y + dir[0]][x + dir[1]] == 9 :
                    if (y + dir[0], x + dir[1]) not in summits:
                        ret+=1
                        summits.append((y + dir[0], x + dir[1]))
                    ret_2 += 1

            elif map[y + dir[0]][x + dir[1]] == (map[y][x] + 1):
                ret_pos, ret_pos_2, summits = score(map, y + dir[0], x + dir[1], summits)
                ret += ret_pos
                ret_2 += ret_pos_2
    return ret, ret_2, summits

sum = 0
sum2 = 0
for y, line in enumerate(map):
    for x, char in enumerate(line):
        if char == 0:
            summit = []
            s, s2, _ = score(map, y, x, summit)
            sum += s
            sum2 += s2

print(f"Partie 1 : {sum}")
print(f"Partie 2 : {sum2}")
