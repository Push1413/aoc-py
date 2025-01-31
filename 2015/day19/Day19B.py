def min_steps(rules, molecule):
    count = 0
    while molecule !="e":
        prev = molecule
        for des, src in rules:
            if des in molecule:
                molecule = molecule.replace(des,src,1)
                count += 1
                print(count,molecule)
                break

        if prev == molecule:
            return -1
    return count


def readInput():
    with open("input.txt","r") as file:
        lines = file.read().splitlines()

    rules = []
    molStr = None
    for line in lines:
        if " => " in line:
            src, des = line.split(" => ")
            rules.append((des, src))
        else:
            molStr = line.strip()
    rules.sort(key=lambda x: len(x[0]), reverse=True)
    print(min_steps(rules,molStr))


if __name__=='__main__':
    readInput()
