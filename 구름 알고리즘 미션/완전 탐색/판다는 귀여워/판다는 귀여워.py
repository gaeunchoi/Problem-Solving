N, M, K = map(int, input().split())
panda = []

for _ in range(K):
	r, c = map(int, input().split())
	panda.append([r, c])

result = float("inf")
for i in range(1, N+1):
	for j in range(1, M+1):
		if [i, j] in panda:
			continue
			
		satisfaction = 0
		for k in range(K):
			distance = (i - panda[k][0])**2 + (j - panda[k][1])**2
			satisfaction += distance
		result = min(result, satisfaction)

print(result)