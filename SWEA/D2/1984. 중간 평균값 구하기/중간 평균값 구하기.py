T = int(input())

for test_case in range(1, T+1):
    nums = list(map(int, input().split()))
    nums.sort()
    print(f'#{test_case} {round(sum(nums[1:9]) / 8)}')