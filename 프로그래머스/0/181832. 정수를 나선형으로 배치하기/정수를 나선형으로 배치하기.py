# 상 하 좌 우 이동을 U, D, L, R로 해서 배열을 벗어나거나 이미 값이 있으면 방향전환
def solution(n):
    answer = [[0] * n for _ in range(n)]
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    x, y = 0, 0
    d = 0

    for i in range(n**2):
        answer[x][y] = i+1
        mx, my = x + directions[d][0], y + directions[d][1]

        if 0 <= mx < n and 0 <= my < n and answer[mx][my] == 0:
            x, y = mx, my
        else:
            d = (d+1) % 4
            x, y = x + directions[d][0], y + directions[d][1]
    return answer