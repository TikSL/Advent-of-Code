# ADVENT-OF-CODE 2024
# Jour 8
# https://adventofcode.com/2024/day/8

# --- Day 8: Resonant Collinearity ---

antennas = {}
x_max = 0
y_max = 0

with open('../inputs/08.txt', 'r') as file:
    lines = file.readlines()
    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            if char != '.':
                if char in antennas.keys():
                    antennas[char].append((x, y))
                else:
                    antennas[char] = [(x, y)]

    x_max = len(lines[0])
    y_max = len(lines)

antinodes_1 = set()
antinodes_2 = set()

for freq in antennas.keys():
    antenna_positions = antennas[freq]
    for i, antennaA in enumerate(antenna_positions):
        if i == len(antenna_positions) - 1:
            break
        for antennaB in antenna_positions[i+1:]:
            for k in range(-x_max, x_max+1):
                x_antinode = antennaB[0] - k * (antennaA[0] - antennaB[0])
                y_antinode = antennaB[1] - k * (antennaA[1] - antennaB[1])
                if 0 <= x_antinode < x_max and 0 <= y_antinode < y_max:
                    antinodes_2.add((x_antinode, y_antinode))
                    if k == 1 or k == -1:
                        antinodes_1.add((x_antinode, y_antinode))

print(f"Partie 1 : {len(antinodes_1)}")
print(f"Partie 2 : {len(antinodes_2)}")
