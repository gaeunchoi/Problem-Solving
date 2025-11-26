N = int(input())
T = []
P = []
dp = [0] * (N + 1)
max_val = 0

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(N - 1, -1, -1):
    time = T[i] + i
    if time <= N:
        dp[i] = max(max_val, P[i] + dp[time])
        max_val = dp[i]
    else:
        dp[i] = max_val

print(max_val)