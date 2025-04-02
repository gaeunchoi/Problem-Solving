T = int(input())

nums = [2, 3, 5, 7, 11]
for tc in range(1, T+1):
    result = [0] * 5
    N = int(input())
    for i in range(5):
        while N % nums[i] == 0:
            result[i] += 1
            N //= nums[i]
    print(f'#{tc} ', end = '')
    print(*result)