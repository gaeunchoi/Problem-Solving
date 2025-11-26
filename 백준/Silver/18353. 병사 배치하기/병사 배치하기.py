N = int(input())
datas = list(map(int, input().split()))
datas.reverse()

dp = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if datas[j] < datas[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))