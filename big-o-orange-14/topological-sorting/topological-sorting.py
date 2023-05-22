import queue

def main():
    V, E = map(int, input().split())
    adj = [[] for _ in range(V)]
    indegree = [0] * V
    result = []

    for _ in range(E):
        u, v = map(int, input().split())
        adj[u - 1].append(v - 1)
        indegree[v - 1] += 1

    topologicalSort(adj, indegree, result)

    if len(result) < V:
        print('Sandro fails.')
        return 0
    
    for x in result:
        print(x + 1, end=' ')

def topologicalSort(adj, indegree, result):
    zeroIndegree = queue.PriorityQueue()

    for i in range(len(indegree)):
        if indegree[i] == 0:
            zeroIndegree.put(i)
    
    while not zeroIndegree.empty():
        u = zeroIndegree.get()
        result.append(u)
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                zeroIndegree.put(v)

if __name__ == "__main__":
    main()