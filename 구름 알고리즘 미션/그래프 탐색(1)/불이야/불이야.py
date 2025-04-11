import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
lab = [list(map(str, input().rstrip())) for _ in range(R)]
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs():
	distance = [[0] * C for _ in range(R)]
	visited = [[False] * C for _ in range(R)]
	q = deque()
	
	for i in range(R):
		for j in range(C):
			if lab[i][j] == '@':
				q.append([i, j])
				visited[i][j] = True
	
	while q:
		cx, cy = q.popleft()
		for dx, dy in directions:
			mx, my = cx + dx, cy + dy
			if 0 <= mx < R and 0 <= my < C and lab[mx][my] != '#' and not visited[mx][my]:
				visited[mx][my] = True
				distance[mx][my] = distance[cx][cy] + 1
				q.append([mx, my])
				
	return distance, visited

dist, visited = bfs()

for i in range(R):
	for j in range(C):
		if lab[i][j] == '&':
			if visited[i][j]:
				print(dist[i][j] - 1)
			else:
				print(-1)