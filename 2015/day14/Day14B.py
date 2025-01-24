import re

def calculateDistance(speed, fly_time, rest_time, elapsed_time):
    # Calculate the distance traveled by a reindeer at a given elapsed time
    cycle_time = fly_time + rest_time
    full_cycles = elapsed_time // cycle_time
    remaining_time = elapsed_time % cycle_time

    # Distance for full cycles
    distance = full_cycles * (speed * fly_time)

    # Add distance for the remaining time if still flying
    if remaining_time <= fly_time:
        distance += speed * remaining_time
    else:
        distance += speed * fly_time

    return distance

def simulateRace(reindeers, race_duration):
    # Initialize a dictionary to keep track of points
    points = {i: 0 for i in range(len(reindeers))}

    for t in range(1, race_duration + 1):
        # Calculate distances at time t for all reindeer
        distances = [calculateDistance(r[0], r[1], r[2], t) for r in reindeers]

        # Find the maximum distance at this time
        max_distance = max(distances)

        # Award points to all reindeer that have the maximum distance
        for i, dist in enumerate(distances):
            if dist == max_distance:
                points[i] += 1

    # Return the maximum points scored by any reindeer
    return max(points.values())

def readInput():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        reindeers = []
        for line in lines:
            # Extract numbers from the input line
            nos = re.findall(r"\d+", line)
            speed = int(nos[0])
            fly_time = int(nos[1])
            rest_time = int(nos[2])
            reindeers.append([speed, fly_time, rest_time])

        # Simulate the race and find the winner
        race_duration = 2503
        result = simulateRace(reindeers, race_duration)
        print("Maximum points:", result)

if __name__=="__main__":
    readInput()

    #2030 too high