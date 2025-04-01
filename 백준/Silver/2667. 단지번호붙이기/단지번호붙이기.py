import sys

N = int(input())

maps = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return 0
    
    if maps[x][y] == 1:
        cnt = 1
        maps[x][y] = 0

        for dx, dy in directions:
            mx, my = x + dx, y + dy
            cnt += dfs(mx, my)

        return cnt
    return 0
    
result = []
for x in range(N):
    for y in range(N):
        block = dfs(x, y)

        if block > 0:
            result.append(block)

result.sort()
print(len(result))
for ele in result:
    print(ele)