import json
def sum_without_code(data):
    if isinstance(data, int):
        return data
    if isinstance(data, list):
        return sum(sum_without_code(item) for item in data)
    if isinstance(data, dict):
        if "red" in  data.values():
            return 0
        return sum(sum_without_code(value) for value in data.values())
    return 0



def readInput():
    f = open(r"input2.txt")
    lines = f.readline()
    parsed_data = json.loads(lines)
    print(sum_without_code(parsed_data))

if __name__ == "__main__":
    readInput()




