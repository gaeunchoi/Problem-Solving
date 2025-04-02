T = int(input())

changes = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for tc in range(1, T+1):
    result = [0] * 8
    N = int(input())

    for i in range(len(changes)):
        cnt = N // changes[i]
        if cnt > 0:
            N = N % changes[i]
            result[i] = cnt

    print(f'#{tc}')
    print(*result)
