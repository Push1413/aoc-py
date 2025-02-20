import math


def isValid(matrix, newRow, newCol):
    row = len(matrix) - 1  # Get the last valid index
    col = len(matrix[0]) - 1 # Get the last valid index
    return 0 <= newRow <= row and 0 <= newCol <= col

def getAdjusentNo(matrix,i,j,numbers):
    direction = [(1,1),(-1,-1),(1,0),(0,1),(1,-1),(-1,1),(-1,0),(0,-1)]
    numbersFound = set()

    for dir in direction:
        newCol = j+ dir[1]
        newRow = i+ dir[0]

        if isValid(matrix,newRow,newCol):
            for item in numbers:
                if item[1]==newRow and item[2]<=newCol<=item[3]:
                    numbersFound.add(item[0])
    if len(numbersFound) == 2:
        return math.prod(numbersFound)
    else:
        return 0

def readInput():
    matrix = []
    numbers = []
    sum =0
    with open("input.txt","r") as file:
        lines = file.readlines()

    for line in lines:
        matrix.append(list(line.strip()))

    row = len(matrix)
    col = len(matrix[0])

    for i in range(row):
        j=0
        while j < col:
            if matrix[i][j].isdigit():
                start = j
                while j< col and matrix[i][j].isdigit():
                    j+=1
                end = j-1
                no = int("".join(matrix[i][start:end+1]))
                numbers.append((no,i,start,end))
            else:
                j+=1

    for i in range(row):
        for j in range(col):
            if matrix[i][j]=="*":
              mulAns = getAdjusentNo(matrix,i,j,numbers)
              sum += mulAns

    print(sum)

if __name__=='__main__':
    readInput()