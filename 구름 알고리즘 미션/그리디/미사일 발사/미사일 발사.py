import sys
input = sys.stdin.readline
from heapq import heappop, heappush

def calcDistance(x, y):
	return (x**2 + y**2) * 2

N = int(input())
start = []
end = []
for _ in range(N):
	X, Y, T = map(int, input().split())
	start.append(T)
	end.append(T + calcDistance(X, Y))
	
hq = []
for i in range(N):
	heappush(hq, (start[i], 1, i))
	heappush(hq, (end[i], 0, i))
	
cnt = result = 0
while hq:
	t, on, i = heappop(hq)
	
	if(on):
		cnt += 1
	else:
		cnt -= 1
	result = max(result, cnt)

answer = 0
for i in range(N):
	answer += end[i] - start[i]
print(answer - result)