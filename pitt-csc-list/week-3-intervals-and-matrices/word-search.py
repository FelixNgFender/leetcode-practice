def exist(board, word):
    def isInBounds(y, x):
        return y >= 0 and y < m and x >= 0 and x < n

    def dfs(y, x, visited, wordIndex):
        if wordIndex == len(word) - 1:
            return True
        visited[y][x] = True
        for deltay, deltax in zip(dy, dx):
            if (
                not isInBounds(y + deltay, x + deltax)
                or visited[y + deltay][x + deltax]
                or board[y + deltay][x + deltax] != word[wordIndex + 1]
            ):
                continue
            elif dfs(y + deltay, x + deltax, visited, wordIndex + 1):
                return True
        visited[y][x] = False
        return False

    m = len(board)
    n = len(board[0])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(m):
        for j in range(n):
            visited = [[False for _ in range(n)] for _ in range(m)]
            if board[i][j] == word[0] and dfs(i, j, visited, 0):
                return True
    return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(exist(board, word))

oard = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"
print(exist(board, word))

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"
print(exist(board, word))

board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
word = "ABCEFSADEESE"
print(exist(board, word))
