import sys
sys.setrecursionlimit(10**8)
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N+1):
    graph[i].sort()

dfs_result = [] * (N+1)
bfs_result = [] * (N+1)
dfs_visited = [False] * (N+1)
bfs_visited = [False] * (N+1)

def dfs(graph, r, visited):
    visited[r] = True
    dfs_result.append(r)

    for node in graph[r]:
        if not visited[node]:
            dfs(graph, node, visited)

def bfs(graph, r, visited):
    q = deque([r])

    visited[r] = True
    bfs_result.append(r)
    
    while q:
        node = q.popleft()
        for v in graph[node]:
            if not visited[v]:
                q.append(v)
                visited[v] = True
                bfs_result.append(v)

dfs(graph, V, dfs_visited)
bfs(graph, V, bfs_visited)

print(*dfs_result)
print(*bfs_result)