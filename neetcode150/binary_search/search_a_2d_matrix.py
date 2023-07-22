def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])

    rowLo, rowHi = 0, m - 1
    colLo, colHi = 0, n - 1
    targetRow = -1

    while rowLo <= rowHi:
        rowMid = (rowLo + rowHi) // 2
        if matrix[rowMid][n - 1] < target:
            rowLo = rowMid + 1
        elif matrix[rowMid][0] > target:
            rowHi = rowMid - 1
        else:
            targetRow = rowMid
            break

    if targetRow == -1:
        return False

    while colLo <= colHi:
        colMid = (colLo + colHi) // 2
        if matrix[targetRow][colMid] < target:
            colLo = colMid + 1
        elif matrix[targetRow][colMid] > target:
            colHi = colMid - 1
        else:
            return True

    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print(searchMatrix(matrix, target))

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13
print(searchMatrix(matrix, target))
