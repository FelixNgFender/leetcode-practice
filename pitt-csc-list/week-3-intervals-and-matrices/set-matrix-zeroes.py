def setZeroes(matrix):
    affectedRows = set()
    affectedCols = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                affectedRows.add(i)
                affectedCols.add(j)

    for row in affectedRows:
        matrix[row] = [0] * len(matrix[0])
    for col in affectedCols:
        for i in range(len(matrix)):
            matrix[i][col] = 0


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
setZeroes(matrix)
print(matrix)

matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
setZeroes(matrix)
print(matrix)
