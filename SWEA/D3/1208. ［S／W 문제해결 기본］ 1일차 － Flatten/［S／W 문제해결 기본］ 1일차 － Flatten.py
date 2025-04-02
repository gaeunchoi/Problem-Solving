for tc in range(1, 11):
    dump = int(input())
    heights = list(map(int, input().split()))

    for i in range(dump):
        heights.sort()
        heights[0] += 1
        heights[-1] -= 1

    print(f'#{tc} {max(heights) - min(heights)}')