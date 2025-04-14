import sys
input = sys.stdin.readline

N = int(input())
tmp = list(map(int, input().split()))
taste = []
for i, v in enumerate(tmp):
	taste.append([v, i])
taste.sort()

valid = True
for i in range(N):
	if taste[i][0] - i <= 0:
		valid = False
		break
		
if not valid:
	print(*range(1, N+1))
else:
	for i in range(N):
		print(taste[i][1] + 1, end = ' ')