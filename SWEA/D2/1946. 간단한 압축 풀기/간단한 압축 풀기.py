T = int(input())

for tc in range(1, T+1):
    N = int(input())
    result = ''

    for _ in range(N):
        alpha, l = input().split()
        result += alpha * int(l)

    print(f'#{tc}')
    for i in range(0, len(result), 10):
        print(result[i:i+10])