import sys
sys.setrecursionlimit(10**8)

N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()

visited = [False] * len(graph)
result = [0 for _ in range(N+1)]
t = 1

def dfs(graph, r, visited):
    global t

    visited[r] = True
    result[r] = t
    t += 1

    for node in graph[r]:
        if not visited[node]:
            dfs(graph, node, visited)

dfs(graph, R, visited)

for i in range(1, N+1):
    print(result[i])