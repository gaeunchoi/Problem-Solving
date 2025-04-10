N, M = map(int, input().split())
current = M * 100 // N
goal = current + 1

left, right = 1, 1000000000000-1
minK = 1000000000000

while left <= right:
	mid = (left + right) // 2
	winrate = (M + mid) * 100 // (N + mid)
	if winrate >= goal:
		minK = mid
		right = mid - 1
	else:
		left = mid + 1

print('X' if minK == 1000000000000 else minK)