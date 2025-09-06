import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
coord = [list(map(int, input().split())) for _ in range(N)]
maxHeight = max(map(max, coord))
direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def BFS(x, y, h, visited):
    visited[x][y] = True
    q = deque([[x, y]])

    while q:
        cx, cy = q.popleft()
        for dx, dy in direction:
            mx, my = cx + dx, cy + dy
            if 0 <= mx < N and 0 <= my < N:
                if not visited[mx][my] and coord[mx][my] > h:
                    visited[mx][my] = True
                    q.append([mx, my])

result = 0
for h in range(0, maxHeight + 1):
    cnt = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if coord[i][j] > h and not visited[i][j]:
                BFS(i, j, h, visited)
                cnt += 1
    result = max(result, cnt)

print(result)