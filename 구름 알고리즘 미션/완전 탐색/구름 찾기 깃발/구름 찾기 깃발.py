N, K = map(int, input().split(" "))
board = [list(map(int, input().split(" "))) for _ in range(N)]
directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

cnt = 0
for x in range(N):
	for y in range(N):
		if board[x][y] == 0:
			clouds = 0
			for dx, dy in directions:
				mx, my = x + dx, y + dy
				if 0 <= mx < N and 0 <= my < N and board[mx][my] == 1:
					clouds += 1
			if clouds == K:
				cnt += 1

print(cnt)