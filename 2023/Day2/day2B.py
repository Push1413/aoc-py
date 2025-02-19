import re

def parsData(drawn):
    colors = {"red": 0, "blue": 0, "green": 0}
    groups = drawn.split(", ")
    for item in groups:
        num_color = item.split()
        if len(num_color) == 2:
            num, color = num_color
            colors[color] = int(num)
    return [colors["red"], colors["blue"], colors["green"]]


def readInput():
    games = {}
    pattern = re.compile(r"Game (\d+): (.*)")
    with open("input.txt","r") as file:
        lines = file.readlines()
    for line in lines:
        match = pattern.match(line)
        if match:
            game_no = int(match.group(1))
            drawsArray = match.group(2).split(";")
            games[game_no] = [parsData(drawn.strip()) for drawn in drawsArray]

    ans = 0
    for game, sets in games.items():
        print(f"Game {game}: {sets}")
        maxR,maxB, maxG = 0,0,0
        for item in sets:
            maxR = max(maxR, item[0])  # Use max() directly
            maxB = max(maxB, item[1])
            maxG = max(maxG, item[2])
        mulAns = maxR* maxB* maxG
        ans += mulAns

    print(ans)


if __name__=='__main__':
    readInput()
    # 14021 is too low
