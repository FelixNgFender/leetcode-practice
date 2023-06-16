from collections import defaultdict


def gameOfLife(board):
    m = len(board)
    n = len(board[0])
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]

    def isInBounds(pos):
        [y, x] = pos
        return y < m and y >= 0 and x < n and x >= 0

    def nextState(pos):
        [y, x] = pos
        neighbors = defaultdict(int)
        for deltay, deltax in zip(dy, dx):
            if isInBounds([y + deltay, x + deltax]):
                neighbors[board[y + deltay][x + deltax]] += 1
        if board[y][x] == 1:
            if neighbors[1] < 2 or neighbors[1] > 3:
                return 0
            else:
                return 1
        else:
            if neighbors[1] == 3:
                return 1
            else:
                return 0

    nextBoard = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            nextBoard[i][j] = nextState([i, j])

    for i, row in enumerate(nextBoard):
        board[i] = row

    print(board)


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
gameOfLife(board)

board = [[1, 1], [1, 0]]
gameOfLife(board)
