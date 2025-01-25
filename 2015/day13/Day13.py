from itertools import permutations

def parse_input(input_data):
    happiness = {}
    for line in input_data.strip().split("\n"):
        parts = line.split()
        person1 = parts[0]
        person2 = parts[-1][:-1]  # Remove the trailing period
        happiness_change = int(parts[3]) * (1 if parts[2] == "gain" else -1)
        happiness[(person1, person2)] = happiness_change
    return happiness

def calculate_happiness(happiness, arrangement):
    total_happiness = 0
    for i in range(len(arrangement)):
        person1 = arrangement[i]
        person2 = arrangement[(i + 1) % len(arrangement)]  # Circular arrangement
        total_happiness += happiness.get((person1, person2), 0)
        total_happiness += happiness.get((person2, person1), 0)
    return total_happiness

def find_max_happiness(happiness, include_self=False):
    people = set(person for pair in happiness.keys() for person in pair)

    if include_self:
        for person in people:
            happiness[("Me", person)] = 0
            happiness[(person, "Me")] = 0
        people.add("Me")

    max_happiness = float("-inf")
    for arrangement in permutations(people):
        max_happiness = max(max_happiness, calculate_happiness(happiness, arrangement))
    return max_happiness

with open("input.txt","r") as file:
    input_data = file.read()
    happiness = parse_input(input_data)
    part1 = find_max_happiness(happiness)
    part2 = find_max_happiness(happiness, include_self=True)

print("Part 1:", part1)  # Maximum happiness without including yourself
print("Part 2:", part2)


