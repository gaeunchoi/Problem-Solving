import sys
from collections import deque
sys.setrecursionlimit(10**8)

N, M, R = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N+1):
    graph[i].sort()

def BFS(graph, r, visited):
    t = 1

    q = deque([r])

    visited[r] = True
    result[r] = t
    t += 1

    while q:
        v = q.popleft()
        for node in graph[v]:
            if not visited[node]:
                q.append(node)
                visited[node] = True
                result[node] = t
                t += 1

result = [0] * (N+1)
visited = [False] * (N+1)
t = 1

BFS(graph, R, visited)

for i in range(1, N+1):
    print(result[i])