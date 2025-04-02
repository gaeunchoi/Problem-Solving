T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        sum = 0
        for j in range(N):
            if maps[i][j] == 1:
                sum += 1
            if maps[i][j] == 0 or j == N-1:
                if sum == K:
                    result += 1
                sum = 0

        for j in range(N):
            if maps[j][i] == 1:
                sum  += 1
            if maps[j][i] == 0 or j == N-1:
                if sum == K:
                    result += 1
                sum = 0
    print(f'#{test_case} {result}')
