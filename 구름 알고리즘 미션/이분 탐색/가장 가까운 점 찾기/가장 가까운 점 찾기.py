import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
X = sorted(map(int, input().split()))

for _ in range(Q):
	p = int(input())
	
	left, right = 0, N-1
	
	while left < right:
		mid = (left + right) // 2
		if X[mid] < p:
			left = mid + 1
		else:
			right = mid
			
	if left == 0:
		print(X[left])
	else:
		print(X[left - 1] if abs(p - X[left-1]) <= abs(p - X[left]) else X[left])