from itertools import groupby

input = "1321131112"
sequence = input
def look_and_say(sequence):
    result = []
    for digit, group in groupby(sequence):
        count = len(list(group))  # Count of the consecutive digits
        result.append(f"{count}{digit}")  # Add count followed by the digit
    return "".join(result)

for i in range(50):
    sequence= look_and_say(sequence)
print(len(sequence))



