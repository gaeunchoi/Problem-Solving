import sys
from collections import deque

T = int(input())
directions = [[-2, 1], [-2, -1], [-1, 2], [-1, -2], [1, 2], [1, -2], [2, 1], [2, -1]]

def bfs():
    q = deque()
    q.append([start_x, start_y])

    while q:
        x, y = q.popleft()

        if x == end_x and y == end_y:
            return maps[x][y] - 1

        for dx, dy in directions:
            mx, my = x + dx, y + dy
            if 0 <= mx < I and 0 <= my < I and not maps[mx][my]:
                maps[mx][my] = maps[x][y] + 1
                q.append([mx, my])

for i in range(T):
    I = int(sys.stdin.readline().rstrip())

    start_x, start_y = map(int, sys.stdin.readline().split())
    end_x, end_y = map(int, sys.stdin.readline().split())

    maps = [[0] * I for _ in range(I)]
    maps[start_x][start_y] = 1

    result = bfs()
    print(result)