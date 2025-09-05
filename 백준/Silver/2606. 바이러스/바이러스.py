import sys
from collections import deque
sys.setrecursionlimit(10**8)

com = int(input())
pair = int(input())

graph = [[] for _ in range(com+1)]

for _ in range(pair):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(com+1):
    graph[i].sort()
  
def bfs(graph, r):
    visited = [False] * (com + 1)
    q = deque([r])
    visited[r] = True
    virus = 0

    while q:
        node = q.popleft()
        for v in graph[node]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
                virus += 1                
    return virus

print(bfs(graph, 1))