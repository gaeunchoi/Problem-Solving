for tc in range(1, 11):
    T = int(input())
    nums = list(map(int, input().split()))

    i = 0
    while True:
        value = nums.pop(0) - (i + 1)
        if value <= 0:
            nums.append(0)
            break
        nums.append(value)
        i = (i + 1) % 5

    print(f'#{T} ', end = ' ')
    print(*nums)