import re

file = open("input.txt","r")
lines = file.readlines()
totalSum =0
for line in lines:
    nosList = re.findall(r"[+-]?\d+",line)
    intList = ([int(nums) for nums in nosList])
    if sum(intList)!=0:
        totalSum += sum(intList)
print(totalSum)


