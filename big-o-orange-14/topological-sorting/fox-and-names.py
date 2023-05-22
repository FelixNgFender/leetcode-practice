def main():
    n = int(input())
    names = []
    for _ in range(n):
        names.append(input())
    adj = [[] for _ in range(26)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            for k in range(min(len(names[i]), len(names[j]))):
                if names[i][k] != names[j][k]:
                    adj[ord(names[i][k]) - ord('a')].append(ord(names[j][k]) - ord('a'))
                    break
            if k == min(len(names[i]), len(names[j])) - 1 and len(names[i]) > len(names[j]):
                print('Impossible')
                exit()
    result = []
    topologicalSort(adj, result)
    for x in result:
        print(chr(x + ord('a')), end='')

def topologicalSort(adj, result):
    V = len(adj)
    visited = [False] * V
    onStack = [False] * V
    for u in range(V - 1, -1, -1):
        if not visited[u]:
            dfs(adj, u, visited, onStack, result)
    result.reverse()

def dfs(adj, u, visited, onStack, result):
    visited[u] = True
    onStack[u] = True
    for v in adj[u]:
        if not visited[v]:
            dfs(adj, v, visited, onStack, result)
        elif onStack[v]:
            print('Impossible')
            exit()
    onStack[u] = False
    result.append(u)

if __name__ == "__main__":
    main()