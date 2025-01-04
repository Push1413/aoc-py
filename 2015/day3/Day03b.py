files = open("input.txt","r")
lines = files.read().strip()
visited_houses = set()
row1, row2 =0,0
col1,col2 =0,0
visited_houses.add((row1, col1))


for move in range(0,len(lines),2):
    if lines[move] == "^":
        row1 -= 1  # Move north
    elif lines[move] == "v":
        row1 += 1  # Move south
    elif lines[move] == ">":
        col1 += 1  # Move east
    elif lines[move] == "<":
        col1 -= 1  # Move west

    visited_houses.add((row1, col1))

for move2 in range(1,len(lines),2):
    if lines[move2] == "^":
        row2 -= 1  # Move north
    elif lines[move2] == "v":
        row2 += 1  # Move south
    elif lines[move2] == ">":
        col2 += 1  # Move east
    elif lines[move2] == "<":
        col2 -= 1  # Move west

    visited_houses.add((row2, col2))

size = len(visited_houses)
print("Visited locations dictionary:", size)