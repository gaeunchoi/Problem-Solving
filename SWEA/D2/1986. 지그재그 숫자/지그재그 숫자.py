T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    result = 0
    for i in range(1, N+1):
        result += i if i % 2 == 1 else -i
    print(f'#{test_case} {result}')