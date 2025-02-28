import math

def readInput():
    with open("input.txt","r") as file:
        lines = file.readlines()
    points =0

    for line in lines:
        divide = line.split(":")
        carddNo = divide[0]
        sides = divide[1].split("|")
        ans = set()
        winingSet = set(map (int, sides[0].strip().split()))
        yourSet = set(map(int,sides[1].strip().split()))
        for item in yourSet:
            if item in winingSet:
                ans.add(item)

        power = len(ans)
        if power !=0:
            points += math.pow(2, (power-1))
    print(points)

if __name__=='__main__':
    readInput()
    #50490 is too high

