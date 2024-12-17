# ADVENT-OF-CODE 2024
# Jour 17
# https://adventofcode.com/2024/day/17

# --- Day 17: Chronospatial Computer ---

A = 0
B = 0
C = 0
program = []

with open("../inputs/17.txt") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        if "Register A: " in line:
            line = line.strip("Register A: ")
            regA = int(line)
        elif "Register B: " in line:
            line = line.strip("Register B: ")
            regB = int(line)
        elif "Register C: " in line:
            line = line.strip("Register C: ")
            regC = int(line)

        elif "Program: " in line:
            line = line.strip("Program: ")
            program = [int(x) for x in (line.split(","))]

A, B, C = regA, regB, regC

# print(f"Registre A: {A}")
# print(f"Register B: {B}")
# print(f"Register C: {C}")
# print(f"Program: {program}")

def get_combo(x):
    return {0: 0, 1: 1, 2: 2, 3: 3, 4: A, 5: B, 6: C}[x]

instruction_pointer = 0
output = []
while True:
    if instruction_pointer>=len(program):
        break
    instruction = program[instruction_pointer]
    operand = program[instruction_pointer + 1]
    combo = get_combo(operand)
    if instruction == 0:
        A = A // 2**combo
        instruction_pointer += 2
    elif instruction == 1:
        B = B ^ operand
        instruction_pointer += 2
    elif instruction == 2:
        B = combo%8
        instruction_pointer += 2
    elif instruction == 3:
        if A != 0:
            instruction_pointer = operand
        else:
            instruction_pointer += 2
    elif instruction == 4:
        B = B ^ C
        instruction_pointer += 2
    elif instruction == 5:
        output.append(int(combo % 8))
        instruction_pointer += 2
    elif instruction == 6:
        B = A // 2**combo
        instruction_pointer += 2
    elif instruction == 7:
        C = A // 2**combo
        instruction_pointer += 2
    # print(f"A: {A}")
    # print(f"B: {B}")
    # print(f"C: {C}")
    # print(f"out: {output}")
    # print(f"ip: {instruction_pointer}")
    # print(f"program: {program}")

answer = ','.join([str(x) for x in output])
print(f"Partie 1 : {answer}")
