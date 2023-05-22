def main():
    n, k = map(int, input().split())
    adj = [[] for _ in range(n)]
    result = []
    studentToBoss = {}
    for i in range(k):
        wishes = list(map(int, input().split()))
        wishes.pop(0)
        for j in range(len(wishes)):
            adj[i].append(wishes[j] - 1)
    topologicalSort(adj, result)
    for i, x in enumerate(result):
        if i == 0:
            studentToBoss[x + 1] = 0
        else:
            studentToBoss[x + 1] = result[i - 1] + 1
    for i in range(1, n + 1):
        print(studentToBoss[i])

def topologicalSort(adj, result):
    V = len(adj)
    visited = [False] * V
    for u in range(V):
        if not visited[u]:
            dfs(adj, u, visited, result)
    result.reverse()

def dfs(adj, u, visited, result):
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            dfs(adj, v, visited, result)
    result.append(u)


if __name__ == "__main__":
    main()