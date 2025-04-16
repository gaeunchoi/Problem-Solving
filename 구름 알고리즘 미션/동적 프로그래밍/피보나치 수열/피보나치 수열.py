import sys
input = sys.stdin.readline
MOD = (10**9) + 7

N = int(input())
dp = [0] * (N + 1)
dp[1], dp[2] = 0, 1

for i in range(3, N+1):
	dp[i] = (dp[i-1] + dp[i-2]) % MOD

print(dp[N])
