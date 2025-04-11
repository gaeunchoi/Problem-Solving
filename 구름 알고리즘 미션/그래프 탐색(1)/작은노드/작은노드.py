import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, N + 1):
    graph[i].sort()

visited = [False] * (N + 1)
count = 0
last_node = 0

def dfs(node):
    global count, last_node
    visited[node] = True
    count += 1

    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)
            return 

    last_node = node

dfs(K)
print(count, last_node)
