N = int(input())
As = list(map(int, input().split(" ")))
result = 2*N + As[0] + As[-1]
for i in range(N-1):
	result += abs(As[i] - As[i+1])
print(result)