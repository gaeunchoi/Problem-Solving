for tc in range(1, 11):
    case = int(input())
    Mat = [list(map(int, input().split())) for _ in range(100)]
    Mat_zip = list(zip(*Mat))

    result, d_left, d_right = 0, 0, 0
    for i in range(100):
        d_right += Mat[i][i]
        d_left += Mat[i][99-i]
        result = max(result, sum(Mat[i]), sum(Mat_zip[i]))

    print(f'#{case} {max(result, d_right, d_left)}')
