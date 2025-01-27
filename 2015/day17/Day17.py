from itertools import combinations

with open("input.txt","r") as file:
    lines = file.readlines()
    li = []
    solution = []
    target = 150
    for i in range(len(lines)):
        li.append(int(lines[i]))

    for r in range(1, len(li)+1):
        for combo in combinations(li,r):
            if sum(combo)== target:
                solution.append(combo)

    print(solution)
    print(len(solution))


    solution2 = []
    foundSmallestR = False
    for r in range(1, len(li)+1):
        for combo in combinations(li,r):
            if sum(combo)== target:
                foundSmallestR = True
                solution2.append(combo)
        if foundSmallestR:
            print(solution2)
            print(len(solution2))
            print(r)
            break


