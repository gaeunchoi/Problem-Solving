T = int(input())

# 우, 하, 좌, 상 순서로 달팽이가 돌아가니까 움직임도 이 순서로 만들자
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for tc in range(1, T+1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]

    x, y = 0, 0
    direc = 0

    for num in range(1, N*N + 1):
        snail[x][y] = num
        mx, my = x + directions[direc][0], y + directions[direc][1]

        if 0 <= mx < N and 0 <= my < N and snail[mx][my] == 0:
            x, y = mx, my
        else:
            direc = (direc + 1) % 4
            x, y = x + directions[direc][0], y + directions[direc][1]

    print(f'#{tc}')
    for r in snail:
        print(*r)
    # print()