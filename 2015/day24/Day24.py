import math
from itertools import combinations

def inputRead():
    nums = []
    with open("input.txt","r") as file:
        lines = file.readlines()
    for line in lines:
        no = int(line.strip())
        nums.append(no)
    return nums

def findGroups(nums,isPart2):
    totalSum = sum(nums)
    comb = []
    min1 = float('inf')
    divisor = 4 if isPart2 else 3
    for i in range(1,len(nums)+1):
        for subset in combinations(nums,i):
            if sum(subset)== totalSum/divisor:
                mul = math.prod(subset)
                if mul < min1:
                    comb.insert(0,subset)
                    min1 = mul
    print(comb, math.prod(comb[0]))


if __name__=='__main__':
    nums = inputRead()
    combination = findGroups(nums,False)
    combination1 = findGroups(nums,True)
