T = int(input())

for tc in range(1, T+1):
    N = int(input())

    result = [0] * 10
    cnt = 0
    while 0 in result:
        current = list(str(N * (cnt+1)))
        for i in current:
            result[int(i)] += 1
        cnt += 1
    print(f'#{tc} {(cnt)*N}')