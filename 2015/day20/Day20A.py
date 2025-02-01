import math

def get_divisors(n):
    divisors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors

def presents_delivered(house):
    """Calculate presents for a house using the modified rule (elf visits 50 houses max)."""
    return sum(d * 10 for d in get_divisors(house))


def find_lowest_house(target):
    """Find the lowest house number that gets at least `target` presents."""
    house = 600000
    while True:
        if presents_delivered(house) >= target:
            return house
        house += 1
        print(house)


if __name__ == '__main__':
    target_presents = 29000000
    result = find_lowest_house(target_presents)
    print(f"The lowest house number to get at least {target_presents} presents is: {result}")