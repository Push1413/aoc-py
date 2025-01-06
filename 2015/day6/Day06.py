import re
import numpy as np

f = open("input.txt","r")
lines = f.readlines()
count =0

# matrix = [[False for _ in range(1000)] for _ in range(1000)]
matrix = np.zeros((1000, 1000), dtype=bool)

for ins in lines:
    row1, col1, row2, col2  = map(int, re.findall(r"\d+",ins))

    if "on" in ins:
        matrix[row1:row2 + 1, col1:col2 + 1] = True  # Correct slicing for both rows and columns

    elif "off" in ins:
        matrix[row1:row2 + 1, col1:col2 + 1] = False  # Update with False

    else:
        matrix[row1:row2 + 1, col1:col2 + 1] = ~matrix[row1:row2 + 1, col1:col2 + 1]  # Toggle using bitwise NOT

for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        if matrix[i][j]:
            count+=1

print(count)
