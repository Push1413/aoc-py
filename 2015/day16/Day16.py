import re

mfcsam = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}


def find_matching_sue(sues, part=1):
    for sue_id, attributes in sues.items():
        match = True
        for key, value in attributes.items():
            if key in mfcsam:
                if part == 1:
                    # Direct comparison for Part 1
                    if mfcsam[key] != value:
                        match = False
                        break
                else:
                    # Adjusted comparison for Part 2
                    if key in ["cats", "trees"]:
                        if value <= mfcsam[key]:
                            match = False
                            break
                    elif key in ["pomeranians", "goldfish"]:
                        if value >= mfcsam[key]:
                            match = False
                            break
                    else:
                        if mfcsam[key] != value:
                            match = False
                            break
        if match:
            return sue_id
    return None

def parse_input(file):
    sues = {}
    with open(file, "r") as f:
        for line in f:
            # Extract Sue number and attributes
            match = re.match(r"Sue (\d+): (.*)", line)
            sue_id = int(match.group(1))
            attributes = match.group(2).split(", ")

            # Store attributes in a dictionary
            sue_info = {}
            for attr in attributes:
                key, value = attr.split(": ")
                sue_info[key] = int(value)

            sues[sue_id] = sue_info
    return sues

if __name__=='__main__':
    sues =  parse_input("input.txt")
    print("Part 1:", find_matching_sue(sues, part=1))
    print("Part 2:", find_matching_sue(sues, part=2))



