nums = list(n**2 for n in map(int, input().split()))
print(sum(nums) % 10)