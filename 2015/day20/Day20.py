import math

def find_house(target):
    max_house = target // 10
    houses = [0] * (max_house + 1)

    for elf in range(1,max_house):
        for house in range(elf,max_house,elf):
            houses[house] += elf * 10
        if houses[elf] >= target:
            return elf
    return None

def find_house2(target):
    max_house = target // 50
    houses = [0] * (max_house + 1)

    for elf in range(1,max_house):
        for house in range(elf,max_house,elf):
            houses[house] += elf * 11
        if houses[elf] >= target:
            return elf
    return None

if __name__ == '__main__':
    target_presents = 29000000
    house = find_house(target_presents)
    print(house)
    house2 = find_house(target_presents)
    print(house2)

# 665281 is too high


