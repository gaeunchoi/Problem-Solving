n, m, k = map(int, input().split())
marble = [[0 for _ in range(n + m + 1)] for _ in range(k+1)]
marble[0][n] = 1

for i in range(k):
	for j in range(1, n + m):
		marble[i+1][j-1] += marble[i][j]
		marble[i+1][j] += marble[i][j]
		marble[i+1][j+1] += marble[i][j]
	print(marble[i+1])
		
result = 0
for i in range(1, k+1):
	result += marble[i][0] + marble[i][n+m]
print(result)