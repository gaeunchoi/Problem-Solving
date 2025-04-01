import sys
sys.setrecursionlimit(10**8)
from collections import deque

N, M = map(int, input().split())

maps = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

def bfs(x, y):
    q = deque()
    q.append([x-1, y-1])

    while q:
        cx, cy = q.popleft()
        for dx, dy in directions:
            mx, my = cx + dx, cy + dy
            if 0 <= mx < N and 0 <= my < M and maps[mx][my] == 1:
                q.append([mx, my])
                maps[mx][my] = maps[cx][cy] + 1

    return maps[N-1][M-1]

result = bfs(1, 1)
print(result)