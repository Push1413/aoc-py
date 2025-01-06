f = open("input.txt","r")
lines = f.readlines()
count =0

def checkGroups(line):
    for i in range(0,len(line)-2):
        for j in range(i+2, len(line)-1):
            if line[i]==line[j] and line[i+1] == line[j+1]:
                return True
    return False


def checkSandwhichLetter(line):
    for i in range(1,len(line)-1):
        prev = line[i-1]
        next = line[i+1]
        if prev==next:
            return True
    return False


for line in lines:
    if checkGroups(line) and checkSandwhichLetter(line):
        count+=1
print(count)