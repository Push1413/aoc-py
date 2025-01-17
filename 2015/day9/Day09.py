import itertools

file = open("input.txt","r")
lines = file.readlines()
distances = {}
locations = set()

for line in lines:
    parts = line.strip().split(" = ")
    loc_pair, dist = parts[0], int(parts[1])
    loc1, loc2 = loc_pair.split(" to ")

    distances[(loc1, loc2)] = dist
    distances[(loc2, loc1)] = dist
    locations.update([loc1,loc2])

    shortest = float("inf")
    longest = float("-inf")

for route in itertools.permutations(locations):
    total_distance = sum(distances[(route[i], route[i + 1])] for i in range(len(route) - 1))
    shortest = min(shortest, total_distance)
    longest = max(longest, total_distance)

print(shortest)
print(longest)

# 443 is too high



