import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node, dist, visited):
    visited[node] = True
    far_node = node
    max_dist = dist

    for next_node in graph[node]:
        if not visited[next_node]:
            temp_node, temp_dist = dfs(next_node, dist + 1, visited)
            if temp_dist > max_dist:
                far_node, max_dist = temp_node, temp_dist

    return far_node, max_dist

visited = [False] * (N + 1)
far_node, _ = dfs(1, 0, visited)

visited = [False] * (N + 1)
_, max_length = dfs(far_node, 0, visited)

print(max_length + 1)
