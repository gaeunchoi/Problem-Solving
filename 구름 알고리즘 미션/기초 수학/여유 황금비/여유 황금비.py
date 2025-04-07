T = int(input())

result = 0
for _ in range(T):
	A, B = map(int, input().split())
	small, big = (A, B) if A < B else (B, A)
	if 1.6 * small <= big <= 1.63 * small:
		result += 1
		
print(result)