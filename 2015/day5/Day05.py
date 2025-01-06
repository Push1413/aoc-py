f = open("input.txt","r")
lines = f.readlines()
count =0
def checkVovels(line):
    vovCount =0;
    vovList = ["a","e","i","o","u"]
    lowerLine = line.lower()
    for str in lowerLine:
        if str in vovList:
            vovCount+=1
        if vovCount>=3:
            return True
    return False

def checkDoubleLetters(line):
    temp = line[0]
    for i in range(1,len(line),1):
        if line[i]==temp:
            return True
        temp = line[i]
    return False

def checkAllowedChar(line):
    groups=[]
    checkList = ["ab","cd","pq","xy"]
    for i in range(0,len(line)-1):
        groups.append(line[i]+line[i+1])
    for group in groups:
        if group in checkList:
            return False
    return True

for line in lines:
    if checkVovels(line) and checkDoubleLetters(line) and checkAllowedChar(line):
        count+=1
print(count)

