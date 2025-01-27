import re

def find_aunt_sue(aunts,gift_giver):
    for sue_no, sue_info in aunts.items():
        match = True
        for key, value in gift_giver.items():
            if key in sue_info and sue_info[key]!=value:
                match = False
                break
            if match:
                return sue_no
    return None

def readInput():
    with open("sample.txt","r") as file:
        lines = file.readlines()
        aunts ={}
        for line in lines:
            parts = line.split(": ", 1)
            sue_number = int(parts[0].split()[1])
            attributes = {}
            for attr in parts[1].split(", "):
                key, value = attr.split(": ")
                attributes[key] = int(value)
            aunts[sue_number] = attributes

        gift_giver = {
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
        print(find_aunt_sue(aunts,gift_giver))

if __name__=='__main__':
    readInput()



