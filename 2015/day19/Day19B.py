import re
import random

def readInput():
    with open("input.txt","r") as file:
        data = file.readlines()
    replacements = []
    molecule = ''
    for line in data:
        if '=>' in line:
            src, dst = line.strip().split(' => ')
            replacements.append((dst, src))  # Reverse the replacements
        elif line.strip():
            molecule = line.strip()
    return replacements, molecule

def reduce_molecule(replacements, molecule):
    steps = 0
    while molecule != 'e':
        for dst, src in replacements:
            if dst in molecule:
                molecule = molecule.replace(dst, src, 1)
                steps += 1
                break
        else:
            # If no replacement was made, shuffle the replacements and reset
            random.shuffle(replacements)
            molecule = target_molecule
            steps = 0
    return steps


if __name__=='__main__':
    replacements, target_molecule = readInput()
    steps_needed = reduce_molecule(replacements, target_molecule)
    print(f"Minimum steps required: {steps_needed}")
