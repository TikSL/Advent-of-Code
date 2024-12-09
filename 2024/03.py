# ADVENT-OF-CODE 2024
# Jour 3
# https://adventofcode.com/2024/day/3

# --- Day 3: Mull It Over ---

counter = 0

def next_real_mul(line):
    end_index = line.index(")")
    if end_index > 11:
        return 0, 0, 4
    else:
        mul = line[4:end_index]
        if ',' in mul:
            mul = mul.split(',')
            a = mul[0]
            b = mul[1]
            if a.isdigit() and b.isdigit():
                return int(a), int(b), end_index
            else:
                return 0, 0, 4
        else:
            return 0, 0, 4

with open('input/03.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        while 'mul(' in line:
            start_index = line.index("mul(")
            line = line[start_index:]
            num_1, num_2, end_index = next_real_mul(line)
            line = line[end_index + 1:]
            counter += num_1 * num_2
    print("Partie 1 : ", counter)


# --- Partie 2 ---

execute = True
counter = 0

with open('input/03.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        while 'mul(' in line:

            start_index = line.index("mul(")

            if 'do()' in line[:start_index]:
                execute = True
            if "don't()" in line[:start_index]:
                execute = False

            line = line[start_index:]
            num_1, num_2, end_index = next_real_mul(line)
            line = line[end_index + 1:]
            if execute:
                counter += num_1 * num_2
    print("Partie 2 : ", counter)
