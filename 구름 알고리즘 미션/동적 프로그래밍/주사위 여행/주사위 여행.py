import sys
input = sys.stdin.readline
MOD = 10 ** 9 + 7

N, M, K = map(int, input().split())

# 휴식: 1, 휴식 x: 0
goormMap = [[0] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    goormMap[r-1][c-1] = 1

caseCnt = [[0] * M for _ in range(N)]
caseCnt[0][0] = 1

rowSum = [[0] * (M + 1) for _ in range(N)]
colSum = [[0] * M for _ in range(N + 1)]

for i in range(N):
    for j in range(M):
        if goormMap[i][j]:
            caseCnt[i][j] = 0
        else:
            if i > 0:
                up = (colSum[i][j] - colSum[max(0, i - 6)][j]) % MOD
                caseCnt[i][j] = (caseCnt[i][j] + up) % MOD
            if j > 0:
                left = (rowSum[i][j] - rowSum[i][max(0, j - 6)]) % MOD
                caseCnt[i][j] = (caseCnt[i][j] + left) % MOD

        rowSum[i][j+1] = (rowSum[i][j] + caseCnt[i][j]) % MOD
        colSum[i+1][j] = (colSum[i][j] + caseCnt[i][j]) % MOD

print(caseCnt[N-1][M-1])
