N = int(input())

nums = list(map(int, input().split()))

ohkensu = [-1] * N

stack = []

for i in range(N):
    while stack and (stack[-1][0] < nums[i]):
        tmp, idx = stack.pop()
        ohkensu[idx] = nums[i]

    stack.append([nums[i], i])

print(*ohkensu)
