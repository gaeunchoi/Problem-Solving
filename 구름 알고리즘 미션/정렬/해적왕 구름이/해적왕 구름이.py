N = int(input())
islands = [];
for i in range(N):
	x, y = map(int, input().split())
	islands.append(((x, y), i))
	
islands.sort()

res = [0] * N

for i in range(N):
	_, idx = islands[i]
	res[idx] = N - i - 1

for i in range(N):
	print(res[i])