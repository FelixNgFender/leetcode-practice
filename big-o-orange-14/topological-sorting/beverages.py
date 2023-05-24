import queue

def main():
    case = 0
    while True:
        try:
            n = int(input())
            beverages = []
            for _ in range(n):
                beverages.append(input())
            m = int(input())
            adj = [[] for _ in range(n)]
            indegree = [0] * n
            for _ in range(m):
                u, v = input().split()
                u = beverages.index(u)
                v = beverages.index(v)
                adj[u].append(v)
                indegree[v] += 1
            result = []
            topologicalSort(adj, indegree, result)
            case += 1
            print('Case #{}: Dilbert should drink beverages in this order: {}.'.format(case, ' '.join(map(lambda u: beverages[u], result))))
            print()
            input()
        except EOFError:
            break

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


if __name__ == '__main__':
    main()