import math

T = int(input())

for tc in range(1, T+1):
    min_value = -1
    N, A, B = map(int, input().split())
    for R in range(1, N+1):
        C = 1
        while R * C <= N:
            value = A * abs(R - C) + B * (N - R * C)
            min_value = value if min_value == -1 else min(min_value, value)
            C += 1

    print(f'#{tc} {min_value}')