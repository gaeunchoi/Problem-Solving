import sys
sys.setrecursionlimit(10**8)

directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

T = int(input())

def dfs(maps, x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return 0
    
    if maps[x][y] == 1:
        value = 1
        maps[x][y] = 0

        for dx, dy in directions:
            value += dfs(maps, x+dx, y+dy)

        return value

    return 0

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    cabbage = [[0] * M for _ in range(N)]
    for i in range(K):
        x, y = map(int, sys.stdin.readline().split())
        cabbage[y][x] = 1
    
    result = []
    for i in range(M):
        for j in range(N):
            bugs = dfs(cabbage, j, i)

            if bugs:
                result.append(bugs)

    print(len(result))