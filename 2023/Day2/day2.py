import re

def parseData(str):
    colors = {"red": 0, "blue": 0, "green": 0}
    groups = str.split(", ")
    for item in groups:
        num_color = item.split()
        if len(num_color) == 2:
            num, color = num_color
            colors[color] = int(num)
    return [colors["red"], colors["blue"], colors["green"]]


def readInput():
    r=12
    g=13
    b = 14
    games = {}
    pattern = re.compile(r"Game (\d+): (.*)")
    with open("input.txt","r") as file:
        lines = file.readlines()
    for line in lines:
        match = pattern.match(line)
        if match:
            game_number = int(match.group(1))
            draws = match.group(2).split(";")

            # Parse all draws and store them as a list
            games[game_number] = [parseData(draw.strip()) for draw in draws]

    ans = 0
    for game, sets in games.items():
        print(f"Game {game}: {sets}")
        shouldAddgame = False
        for i in sets:
            if i[0]<=r and i[1]<=b and i[2]<=g:
                shouldAddgame = True
            else:
                shouldAddgame = False
                break
        if shouldAddgame:
            ans +=game

    print(ans)


if __name__=='__main__':
    readInput()

    #18190 is too high
