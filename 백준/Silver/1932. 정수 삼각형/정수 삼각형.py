N = int(input())

dp = []
for i in range(N):
    dp.append(list(map(int, input().split())))

for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            left = 0
        else:
            left = dp[i - 1][j - 1]

        if j == i:
            right = 0
        else:
            right = dp[i - 1][j]

        dp[i][j] += max(left, right)

print(max(dp[N -1]))
