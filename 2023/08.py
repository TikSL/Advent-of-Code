# ADVENT-OF-CODE 2023
# Jour 8
# https://adventofcode.com/2023/day/8

# --- Day 8: Haunted Wasteland ---

lines = open('08.txt', 'r').readlines()

# inputs découpé : plus simple

# pattern_deplacement = "LLLRLRLRLLRRRLRRRLRRRLLLRLRLLRRLLRRLRLRLLRLRLRRLLRRRLRLLRRLRRRLRRLLLRRRLRRRLRRRLLLLRRLRRRLRLRRRLRRLLRLRLRRRLRRRLRRLRRRLLLLLLRLRRRLLLLRLRRRLRRRLRLRRLRLRLRLRLRRRLLRRLRLRRLRRLRRLLRLLLRRLRLLRRLRLRRLRRRLRRLLRLRLRLRRLLRLLRRLLLRLRLRRRLRRLLRRRLRLRLRRLLRLRLRLRRLRLRLRRLRRLLRRLRRRLRRRLLLRRRR"
pattern_deplacement ="LR"
correspondances = {}

for line in lines:
    line = line.strip()
    [dep, arr] = line.split(" = ")
    arr = arr.replace("(", "")
    arr = arr.replace(")", "")
    correspondances[dep] = [arr.split(", ")[0],arr.split(", ")[1]]

#
# pos = 'AAA'
# steps = 0
# index = steps % len(pattern_deplacement)
# while pos != "ZZZ":
#     # print(pattern_deplacement[index])
#     if pattern_deplacement[index] == "L":
#         pos = correspondances[pos][0]
#     else:
#         pos = correspondances[pos][1]
#     steps += 1
#     index = steps % len(pattern_deplacement)
# print("PARTIE 1 ",steps)
# steps1 = steps
# Partie 2

correspondances = {}

for line in lines:
    line = line.strip()
    [dep, arr] = line.split(" = ")
    arr = arr.replace("(", "")
    arr = arr.replace(")", "")
    correspondances[dep] = [arr.split(", ")[0],arr.split(", ")[1]]


positions = []
for pos in correspondances.keys():
    if pos[2] == "A":
        positions.append(pos)

def pos_ok(positions):
    for pos in positions:
        if pos[2] != "Z":
            return False
    return True

# z = []
# for position in positions:
#
#     pos = position
#     print(pos)
#     pos_z=[]
#     steps = 0
#     index = steps % len(pattern_deplacement)
#     while steps < 20000000:
#         # print(pos[2])
#         if pos[2] == 'Z':
#             # print("z")
#             pos_z.append(steps)
#         if pattern_deplacement[index] == 'L':
#             pos = correspondances[pos][0]
#         else:
#             pos = correspondances[pos][1]
#         # print(pos)
#         steps += 1
#         index = steps % len(pattern_deplacement)
#     z.append(pos_z)
#
# for x in z:
#     print(x)
#
# for i in range(len(z)):
#     z[i] = set(z[i])
#
# commum = z[0] & z[1]
# print(commum)
#
# commum = commum & z[2]
# print(commum)
#
# commum = commum & z[3]
# print(commum)
#
# commum = commum & z[4]
# print(commum)
#
# commum = commum & z[5]
# print(commum)

steps = 0
positions = ["AAA"]
index = steps % len(pattern_deplacement)
while steps < 2000000:
# while not pos_ok(positions):

    if pattern_deplacement[index] == "L":
        for i,pos in enumerate(positions):
            positions[i] = correspondances[pos][0]
            if positions[i][2] == 'Z':
                print(index)
    else:
        for i,pos in enumerate(positions):
            positions[i] = correspondances[pos][1]
            if positions[i][2]== 'Z':
                print(index)
    # print(positions)
    steps += 1
    index = steps % len(pattern_deplacement)
print(positions)
print("PARTIE 2 :",steps)
