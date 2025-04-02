T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = []

    if N > M:
        for i in range(0, N - M + 1):
            value = 0
            for j in range(M):
                value += A[j+i] * B[j]
            result.append(value)
    else:
        for i in range(0, M - N + 1):
            value = 0
            for j in range(N):
                value += A[j] * B[j+i]
            result.append(value)

    print(f'#{tc} {max(result)}')