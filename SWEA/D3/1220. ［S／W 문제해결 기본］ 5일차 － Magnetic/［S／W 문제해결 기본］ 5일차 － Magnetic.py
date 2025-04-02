for tc in range(1, 11):
    l = int(input())
    table = [list(map(int, input().split())) for _ in range(l)]

    result = 0
    for i in range(l):
        flag = False
        for j in range(l):
            if table[j][i] == 1:
                flag = True
            if table[j][i] == 2 and flag == True:
                result += 1
                flag = False
    print(f'#{tc} {result}')