import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]

# 사과 체크
for _ in range(K):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1

# 이동시간 + 방향 체크
L = int(input())
turns = {}
for _ in range(L):
    X, C = input().split()
    turns[int(X)] = C

directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
idx_d = 0

snake = deque([(0, 0)])
body = set([(0, 0)])
cx, cy = 0, 0
time = 0

while True:
    time += 1
    mx, my = cx + directions[idx_d][0], cy + directions[idx_d][1]

    if not (0 <= mx < N and 0 <= my < N) or (mx, my) in body:
        print(time)
        break

    snake.appendleft((mx, my))
    body.add((mx, my))

    if board[mx][my] == 1:
        board[mx][my] = 0
    else:
        tx, ty = snake.pop()
        body.remove((tx, ty))

    cx, cy = mx, my

    # 시간 맞춰 회전하자
    if time in turns:
        if turns[time] == 'D':
            idx_d = (idx_d + 1) % 4
        else:
            idx_d = (idx_d - 1) % 4