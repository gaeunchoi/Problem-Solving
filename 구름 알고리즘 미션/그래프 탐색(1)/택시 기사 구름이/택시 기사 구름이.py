import sys
from collections import deque
input = sys.stdin.readline

directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

def bfs(start, end):
	distance = [[-1] * N for _ in range(N)]
	distance[start[0]][start[1]] = 0
	q = deque([start])
	
	while q:
		cx, cy = q.popleft()
		for dx, dy in directions:
			mx, my = cx + dx, cy + dy
			if 0 <= mx < N and 0 <= my < N and goormMap[mx][my] != 1 and distance[mx][my] == -1:
				distance[mx][my] = distance[cx][cy] + 1
				q.append([mx, my])
	return distance[end[0]][end[1]]
	

N, M = map(int, input().split())
X, Y, Z = map(int, input().split())
goormMap = [list(map(int, input().split())) for _ in range(N)]
customer = [list(map(int, input().split())) for _ in range(M)]

result = 0
cy, cx = customer[0][0] - 1, customer[0][1] - 1

for i in range(M):
	sy, sx, ey, ex = [x-1 for x in customer[i]]
	
	if i == 0:
		moveDis = 0
	else:
		moveDis = bfs([cx, cy], [sx, sy])
	workDis = bfs([sx, sy], [ex, ey])

	if workDis <= 5:
		charge = X
	else:
		charge = X + (workDis - 5) * Y
	
	result += (charge - (moveDis + workDis) * Z)
	
	cx, cy = ex, ey
print(result)
	