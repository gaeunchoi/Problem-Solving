def isPrime(n):
	for i in range(2, int(n ** (1/2)) + 1):
		if n % i == 0:
			return False
	return True

N = int(input())

for _ in range(N):
	A = int(input())
	print("Yes" if isPrime(A) else "No")