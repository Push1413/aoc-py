# # => on and . => off

def checkIsValid(matrix,newRow,newCol):
    if not matrix or not matrix[0]:
        return False
    rowSize = len(matrix)
    colSize = len(matrix[0])
    return 0 <= newRow < rowSize and 0 <= newCol < colSize

def count_on_neighbors(matrix,row,col):
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1,-1],[-1,1],[1,-1],[1,1]]
    noOfOnLights = 0
    for dirRow, dirCol in directions:
        newRow = row + dirRow
        newCol = col + dirCol

        if checkIsValid(matrix, newRow,newCol):
            if matrix[newRow][newCol]=='#':
                noOfOnLights+=1
    return noOfOnLights

def keep_corners_on(grid):
    rows, cols = len(grid), len(grid[0])
    corners = [(0, 0), (0, cols - 1), (rows - 1, 0), (rows - 1, cols - 1)]
    for r, c in corners:
        grid[r][c] = '#'

def simulate_step(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = [['.' for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            on_neighbors = count_on_neighbors(grid, r, c)
            if grid[r][c] == '#' and on_neighbors in (2, 3):
                new_grid[r][c] = '#'
            elif grid[r][c] == '.' and on_neighbors == 3:
                new_grid[r][c] = '#'
    return new_grid



def readInput():
    with open("input.txt","r") as file:
        matrix = []
        lines = file.readlines()
        for line in lines:
            list1 = list(line.strip())
            matrix.append(list1)

        for i in range(100):
            matrix = simulate_step(matrix)
            keep_corners_on(matrix)

        total_on = sum(row.count('#') for row in matrix)

        print(total_on)

if __name__=='__main__':
     readInput()





