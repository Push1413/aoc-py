import re

def calculateDistance(speed,time,rest):
    winingSec = 2503
    division = winingSec // (time+rest)
    reminder = winingSec % (time+rest)
    distancesDrove = speed* time * division

    for i in range(reminder):
        if time!=0:
            distancesDrove +=speed
            time-=1
    return distancesDrove

def readInput():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        winingDistance = 0
        for line in lines:
            nos = re.findall(r"\d+",line)
            speed = int(nos[0])
            time = int(nos[1])
            rest = int(nos[2])
            dist = calculateDistance(speed,time,rest)
            winingDistance = max(winingDistance,dist)
        print(winingDistance)

if __name__=="__main__":
    readInput()


