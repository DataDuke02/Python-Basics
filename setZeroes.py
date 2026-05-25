#Given an m x n matrix, if an element is 0, set its entire row and column to 0

def setZeroes(matrix):
    row_zero = any(matrix[i][0] == 0 for i in range(len(matrix)))
    col_zero = any(matrix[0][j] == 0 for j in range(len(matrix[0])))

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if row_zero:
        for i in range(len(matrix)):
            matrix[i][0] = 0
    if col_zero:
        for j in range(len(matrix[0])):
            matrix[0][j] = 0
