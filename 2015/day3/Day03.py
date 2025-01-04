files = open("input.txt","r")
lines = files.read().strip()
visited_houses = set()
row =0
col =0
visited_houses.add((row, col))

for move in lines:
    if move == "^":
        row -= 1  # Move north
    elif move == "v":
        row += 1  # Move south
    elif move == ">":
        col += 1  # Move east
    elif move == "<":
        col -= 1  # Move west

    visited_houses.add((row, col))

size = len(visited_houses)
print("Visited locations dictionary:", size)

# 1731 is too low




