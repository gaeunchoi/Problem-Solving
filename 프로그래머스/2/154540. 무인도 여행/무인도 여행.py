from collections import deque

def solution(maps):
    answer = []
    maps = [list(row) for row in maps]
    M = len(maps)
    N = len(maps[0])
    ds = [[-1, 0], [0, -1], [1, 0], [0, 1]]

    def bfs(x, y):
        nums = int(maps[x][y])
        maps[x][y] = 'X'
        q = deque([[x, y]])

        while q:
            cx, cy = q.popleft()

            for dx, dy in ds:
                mx, my = cx + dx, cy + dy
                if 0 <= mx < M and 0 <= my < N and maps[mx][my] != 'X':
                    nums += int(maps[mx][my])
                    q.append([mx, my])
                    maps[mx][my] = 'X'

        return nums

    for i in range(M):
        for j in range(N):
            if maps[i][j] != 'X':
                answer.append(bfs(i, j))

    return sorted(answer) if len(answer) != 0 else [-1]