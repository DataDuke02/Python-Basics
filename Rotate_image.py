# You are given an n x n 2D matrix representing an image, rotate the image by
# 90 degrees (clockwise)


def rotate(matrix):
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n- i- 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n- j- 1][i]
            matrix[n- j- 1][i] = matrix[n- i- 1][n- j- 1]
            matrix[n- i- 1][n- j- 1] = matrix[j][n- i- 1]
            matrix[j][n- i- 1] = temp
