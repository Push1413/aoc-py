def updateRegister(arr, pointer, a, b):
    ins = arr[0]
    reg = arr[1]  # No need to strip the comma here; handle it in the match

    if ins == "jio":
        poi = int(arr[2])
        match reg.strip(','):  # Remove comma for matching
            case 'a':  # Consistent case
                if a == 1:
                    pointer += poi
                else:
                    pointer += 1
            case 'b':  # Consistent case
                if b == 1:
                    pointer += poi
                else:
                    pointer += 1

    elif ins == "jie":
        poi = int(arr[2])
        match reg.strip(','):  # Remove comma for matching
            case 'a':  # Consistent case
                if a % 2 == 0:
                    pointer += poi
                else:
                    pointer += 1
            case 'b':  # Consistent case
                if b % 2 == 0:
                    pointer += poi
                else:
                    pointer += 1

    elif ins == "jmp":
        jump = int(reg)
        pointer += jump

    elif ins == "inc":
        pointer += 1
        match reg:  # No comma here
            case 'a':
                a += 1
            case 'b':
                b += 1

    elif ins == "tpl":
        pointer += 1
        match reg:  # No comma here
            case 'a':
                a = a * 3
            case 'b':
                b = b * 3

    elif ins == "hlf":
        pointer += 1
        match reg.strip(','):  # Remove comma for matching
            case 'a':
                a = a / 2
            case 'b':
                b = b / 2

    return a, b, pointer

def readInput(isPartB):
    if isPartB:
        a=1
    else:
        a =0
    b=0
    with open("input.txt","r") as file:
        lines = file.readlines()
    pointer =0
    print(f"length is {len(lines)}")
    while True:
        if pointer >= len(lines):
            break
        else:
            line = lines[pointer]
            lineArr = line.split()
            a,b, pointer = updateRegister(lineArr,pointer,a,b)

    return b

if __name__=="__main__":
    print(readInput(True))
