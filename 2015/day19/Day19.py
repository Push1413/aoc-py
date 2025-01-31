import re

def generate_molecules(rules, molecule):
    unique_molecules = set()

    for src, dst in rules:
        for match in re.finditer(src, molecule):  # Find all occurrences of src
            start = match.start()
            new_molecule = molecule[:start] + dst + molecule[start+len(src):]
            unique_molecules.add(new_molecule)

    return unique_molecules

def readInput():
    with open("input.txt","r") as file:
        lines = file.readlines()
    lib = []
    molStr = None
    for line in lines:
        if " => " in line:
            src, des = line.strip().split(" => ")
            lib.append((src,des))
        else:
            molStr = line.strip()
    uniMol = generate_molecules(lib,molStr)
    print(len(uniMol))

if __name__=='__main__':
    readInput()

    #214 is too low
    #697 is too high

