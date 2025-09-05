import sys
from collections import deque

input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())


def BFS():
    visited = [False] * (F + 1)
    distance = [-1] * (F + 1)
    q = deque([S])
    visited[S] = True
    distance[S] = 0

    while q:
        cur = q.popleft()
        if cur == G:
            return distance[cur]

        up = cur + U
        down = cur - D
        if up <= F and not visited[up]:
            q.append(up)
            visited[up] = True
            distance[up] = distance[cur] + 1
        if 1 <= down and not visited[down]:
            q.append(down)
            visited[down] = True
            distance[down] = distance[cur] + 1

    return -1


result = BFS()
print(result if result != -1 else 'use the stairs')