def divide_pow(n, m):
    value = 0
    if m == 1:
        return n
    if m % 2 == 0:
        return divide_pow(n, m//2) * divide_pow(n, m//2)
    else:
        return divide_pow(n, m//2) * divide_pow(n, m//2) * n

for _ in range(1, 11):
    case = int(input())
    N, M = map(int, input().split())

    result = divide_pow(N, M)
    print(f'#{case} {result}')