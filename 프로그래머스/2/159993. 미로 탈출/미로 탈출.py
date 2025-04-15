from collections import deque

def solution(maps):
    directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    N, M = len(maps), len(maps[0])
    
    def bfs(s, e):
        visited = [[False] * M for _ in range(N)]
        visited[s[0]][s[1]] = True
        q = deque([[s, 0]])
        
        while q:
            [x, y], dist = q.popleft()
            if x == e[0] and y == e[1]:
                return dist
            
            for dx, dy in directions:
                mx, my = x + dx , y + dy
                if 0 <= mx < N and 0 <= my < M and not visited[mx][my] and maps[mx][my] != 'X':
                    q.append([[mx, my], dist+1])
                    visited[mx][my] = True
        return -1
    
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S':
                S = [i, j]
            elif maps[i][j] == 'L':
                L = [i, j]
            elif maps[i][j] == 'E':
                E = [i, j]
                
                
    S_to_L = bfs(S, L)
    L_to_E = bfs(L, E)
    if S_to_L < 0 or L_to_E < 0:
        return -1
    else:
        return S_to_L + L_to_E
                