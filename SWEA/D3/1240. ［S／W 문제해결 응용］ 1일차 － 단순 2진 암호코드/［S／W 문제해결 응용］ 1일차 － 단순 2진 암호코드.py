T = int(input())

nums = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Mat = [list(map(int, input().rstrip())) for _ in range(N)]

    answer = []
    for i in range(N):
        if 1 in Mat[i]:
            for j in range(M-1, 0, -1):
                if Mat[i][j] == 1:
                    tmp = Mat[i][j - 55 : j+1]
                    for k in range(8):
                        answer.append(nums.index(''.join(str(x) for x in tmp[7 * k: 7 * (k + 1)])))
                    break
            break

    sum1, sum2 = 0, 0
    for i in range(1, 9):
        if i % 2 == 1:
            sum1 += answer[i-1]
        else:
            sum2 += answer[i-1]

    result = sum(answer) if (sum1 * 3 + sum2) % 10 == 0 else 0
    print(f'#{tc} {result}')