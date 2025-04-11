from collections import deque
N, M = map(int, input().split())
picture = [list(map(str, input().rstrip())) for _ in range(M)]
directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
visited = [[False] * N for _ in range(M)]

def BFS(x, y):
	extent = 1
	q = deque([[x, y]])
	visited[x][y] = True
	
	while q:
		cx, cy = q.popleft()
		for dx, dy in directions:
			mx, my = cx + dx, cy + dy
			if 0 <= mx < M and 0 <= my < N and picture[mx][my] == '#' and not visited[mx][my]:
					q.append([mx, my])
					visited[mx][my] = True
					extent += 1
		
	return extent;
	
	
cnt = 0
max_block_size = 0
for i in range(M):
	for j in range(N):
		if picture[i][j] == '#' and not visited[i][j]:
			cnt += 1
			max_block_size = max(max_block_size, BFS(i, j))

print(cnt)
print(max_block_size)