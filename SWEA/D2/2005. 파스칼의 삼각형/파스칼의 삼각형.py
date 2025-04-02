T = int(input())
for test_case in range(1, T+1):
    print(f'#{test_case}')
    N = int(input())
    result = [[] for _ in range(N)]

    for i in range(N):
        for j in range(i+1):
            if i == 0 or j == 0 or j == i:
                result[i].append(1)
            else:
                result[i].append(result[i-1][j-1] + result[i-1][j])


    for ele in result:
        print(*ele)
