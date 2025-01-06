import re
import numpy as np

f = open("input.txt","r")
lines = f.readlines()
count =0

matrix = np.zeros((1000, 1000),dtype=int)
for ins in lines:
    row1, col1, row2, col2  = map(int, re.findall(r"\d+",ins))

    if "on" in ins:
        matrix[row1:row2 + 1, col1:col2 + 1] +=1  # Correct slicing for both rows and columns

    elif "off" in ins:
        temp_matrix = matrix[row1:row2 + 1, col1:col2 + 1] -1
        temp_matrix[temp_matrix < 0] = 0
        matrix[row1:row2 + 1, col1:col2 + 1] = temp_matrix  # Update with False

    else:
        matrix[row1:row2 + 1, col1:col2 + 1] += 2  # Toggle using bitwise NOT
print(matrix.sum())

