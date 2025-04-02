T = int(input())

def check(cx, cy):
    result = 0

    for i in range(cx, cx+M):
        for j in range(cy, cy+M):
            if 0 <= i < N and 0 <= j < N:
                result += maps[i][j]
    return result

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(N):
            result = max(result, check(i, j))

    print(f'#{test_case} {result}')