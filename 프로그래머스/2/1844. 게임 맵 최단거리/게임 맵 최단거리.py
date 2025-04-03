from collections import deque
def solution(maps):
    N, M = len(maps), len(maps[0])
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    q = deque([[0, 0, 1]])
    while q:
        x, y, distance = q.popleft()
        if x == N-1 and y == M-1:
            return distance
        for dx, dy in directions:
            mx, my = x + dx, y + dy
            if 0 <= mx < N and 0 <= my < M and maps[mx][my] == 1 and not visited[mx][my]:
                visited[mx][my] = True
                q.append([mx, my, distance+1])
    
    return -1