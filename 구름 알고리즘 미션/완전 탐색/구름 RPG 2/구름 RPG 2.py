N = int(input())
A = [int(input()) for _ in range(N)]

def is_prime(n):
	for i in range(2, int(n ** 0.5) + 1):
		if not n % i:
			return False
	return True

for i in range(N):
	result = 0
	while not is_prime(A[i] - result):
		result += 1
	print(result)