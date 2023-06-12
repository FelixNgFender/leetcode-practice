def spiralOrder(matrix):
    def isInBounds(y, x):
        return y >= 0 and y <= m - 1 and x >= 0 and x <= n - 1
    if len(matrix) == 0:
        return []
    m = len(matrix)
    n = len(matrix[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    x = 0
    y = 0
    # 0: l -> r, 1: u -> b, 2: r -> l, 3: b -> u
    direction = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    res = []
    while len(res) < m * n:
        res.append(matrix[y][x])
        visited[y][x] = True
        if (not isInBounds(y + dy[direction], x + dx[direction])) or visited[y + dy[direction]][x + dx[direction]]:
            direction = (direction + 1) % len(dx)
        y, x = y + dy[direction], x + dx[direction]
    return res
