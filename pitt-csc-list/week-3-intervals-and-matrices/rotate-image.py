def rotate(matrix):
    n = len(matrix)
    matrix.reverse()
    for i in range(1, n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate(matrix))

matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
print(rotate(matrix))
