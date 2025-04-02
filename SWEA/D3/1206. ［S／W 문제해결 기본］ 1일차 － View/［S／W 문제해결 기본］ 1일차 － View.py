for tc in range(1, 11):
    N = int(input())
    heights = list(map(int, input().split()))

    result = 0

    for i in range(2, N-2):
        max_h = max(heights[i-1], heights[i-2], heights[i+1], heights[i+2])
        if heights[i] > max_h:
            result += heights[i] - max_h

    print(f'#{tc} {result}')