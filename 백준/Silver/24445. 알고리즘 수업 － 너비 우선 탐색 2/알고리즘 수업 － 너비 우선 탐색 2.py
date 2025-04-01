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
    graph[i].sort(reverse = True)

visited = [0] * (N+1)

def bfs(graph, r):
    global visited
    q = deque([r])

    visited[r] = 1
    t = 2

    while q:
        node = q.popleft()

        for v in graph[node]:
            if visited[v] == 0:
                q.append(v)
                visited[v] = t
                t += 1

bfs(graph, R)

for i in range(1, N+1):
    print(visited[i])