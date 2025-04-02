nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())
for tc in range(1, T+1):
    case, N = input().split()
    messages = list(input().split())
    result = [0] * 10

    for i in range(10):
        result[i] = messages.count(nums[i])

    print(f'#{tc}')
    for i in range(10):
        print((nums[i] + ' ') * result[i], end = ' ')