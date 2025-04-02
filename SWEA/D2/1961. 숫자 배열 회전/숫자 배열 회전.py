T = int(input())

def rotate_matrix(target, result):
    for i in range(N):
        for j in range(N):
            result[i][j] = target[N-1-j][i]

    return result

for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]

    degree90, degree180, degree270 = [[[0] * N for _ in range(N)] for _ in range(3)]
    degree90 = rotate_matrix(M, degree90)
    degree180 = rotate_matrix(degree90, degree180)
    degree270 = rotate_matrix(degree180, degree270)

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(degree90[i][j], end = '')
        print(end = ' ')
        for j in range(N):
            print(degree180[i][j], end='')
        print(end = ' ')
        for j in range(N):
            print(degree270[i][j], end='')
        print()
