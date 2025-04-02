def dfs(x, cnt):
    global result
    visited[x] = 1

    for i in graph[x]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, cnt + 1)
    visited[x] = 0
    if result < cnt:
        result = cnt

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    result = 0

    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, N+1):
        visited = [0] * (N+1)
        dfs(i, 1)

    print(f'#{tc} {result}')
