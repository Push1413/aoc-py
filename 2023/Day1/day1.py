import re
def readInput():
    totalSum = 0
    with open("input.txt","r") as file:
        lines = file.readlines()
    for line in lines:
        nos = re.findall(r"\d",line)
        str = nos[0] + nos[-1]
        no = int(str)
        totalSum +=no
    return totalSum

def readInputPart2():
    totalSum = 0
    dict = {
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9"
    }
    pattern = re.compile(r"one|two|three|four|five|six|seven|eight|nine|\d")
    pattern = re.compile(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))")
    with open("input.txt","r") as file:
        lines = file.readlines()
    for line in lines:
        matches = [dict[m] if m in dict else m for m in re.findall(pattern, line)]
        # Get the first and last extracted number
        first, last = matches[0], matches[-1]
        totalSum += int(first+last)
    return totalSum


if __name__=='__main__':
    print(readInput())
    print(readInputPart2())
