# Given ingredient properties
ingredients = {
    "Sugar":   [3, 0, 0, -3, 2],
    "Sprinkles": [-3, 3, 0, 0, 9],
    "Candy":   [-1, 0, 4, 0, 1],
    "Chocolate":[0, 0, -2, 2, 8]
}

def compute_score(amounts, part2=False):
    totals = [0] * 5  # Capacity, Durability, Flavor, Texture, Calories

    # Calculate property sums
    for i, (ing, values) in enumerate(ingredients.items()):
        for j in range(5):
            totals[j] += values[j] * amounts[i]

    # Ensure non-negative values
    for i in range(4):
        if totals[i] < 0:
            totals[i] = 0

    # Compute cookie score
    score = totals[0] * totals[1] * totals[2] * totals[3]

    # Part 2: Check for 500 calories
    if part2 and totals[4] != 500:
        return 0

    return score

best_score_part1 = 0
best_score_part2 = 0

for a in range(101):
    for b in range(101 - a):
        for c in range(101 - a - b):
            d = 100 - a - b - c  # Ensure sum is exactly 100
            amounts = [a, b, c, d]
            best_score_part1 = max(best_score_part1, compute_score(amounts))
            best_score_part2 = max(best_score_part2, compute_score(amounts, part2=True))

print("Part 1:", best_score_part1)
print("Part 2:", best_score_part2)

