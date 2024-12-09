# ADVENT-OF-CODE 2024
# Jour 7
# https://adventofcode.com/2024/day/7

# --- Day 7: Bridge Repair ---

operations = {}

with open('input/07.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        line = line.split(':')
        target = int(line[0])
        terms = [int(x) for x in (line[1].strip().split(' '))]
        operations[target] = terms

count_1 = 0
count_2 = 0

def possible_1(target_number, number_list):
    if len(number_list) == 1:
        return number_list[0] == target_number
    else:
        if possible_1(target_number, [number_list[0] + number_list[1]] + number_list[2:]):
            return True
        if possible_1(target_number, [number_list[0] * number_list[1]] + number_list[2:]):
            return True
        return False

def possible_2(target_number, number_list):
    if len(number_list) == 1:
        return number_list[0] == target_number
    else:
        if possible_2(target_number, [number_list[0] + number_list[1]] + number_list[2:]):
            return True
        if possible_2(target_number, [number_list[0] * number_list[1]] + number_list[2:]):
            return True
        if possible_2(target_number, [int(str(number_list[0]) + str(number_list[1]))] + number_list[2:]):
            return True
        return False

for target_to_test in operations.keys():
    numbers = operations[target_to_test]
    if possible_1(target_to_test, numbers):
        count_1 += target_to_test
    if possible_2(target_to_test, numbers):
        count_2 += target_to_test

print(f"Partie 1 : {count_1}")
print(f"Partie 2 : {count_2}")
