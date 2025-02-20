def isValid(matrix, newRow, newCol):
    row = len(matrix) - 1  # Get the last valid index
    col = len(matrix[0]) - 1 # Get the last valid index
    return 0 <= newRow <= row and 0 <= newCol <= col

def check(matrix, startRow, startCol, endCol):
    direction = [(1,1),(-1,-1),(1,0),(0,1),(1,-1),(-1,1),(-1,0),(0,-1)]

    for j in range(startCol,endCol+1):
        for dir in direction:
            newRow = startRow+dir[0]
            newCol = j+dir[1]

            if isValid(matrix, newRow, newCol):
                if not matrix[newRow][newCol].isdigit() and matrix[newRow][newCol]!=".":
                    return True
    return False

def readInput():
    matrix = []
    with open("input.txt","r") as file:
        lines = file.readlines()

    for line in lines:
        list1 = list(line.strip())
        matrix.append(list1)

    row = len(matrix)
    col = len((matrix[0]))
    ans =0
    for i in range(row):
        j =0
        while j < col:
            if matrix[i][j].isdigit():
                start = j
                while j<col and matrix[i][j].isdigit():
                    j+=1
                end = j-1
                no = int("".join(matrix[i][start:end+1]))
                if check(matrix,i,start,end):
                    ans +=no
            j+=1
    print(ans)


if __name__== '__main__':
    readInput()
    # 8504 is too low
    # 564267 is too high







