N = int(input())
Rg, Cg = map(int, input().split())
Rp, Cp = map(int, input().split())
Rg, Cg, Rp, Cp = Rg - 1, Cg - 1, Rp - 1, Cp - 1

directions = {'L': [0, -1], 'R': [0, 1], 'U': [-1, 0], 'D': [1, 0]}

order = [list(input().split()) for _ in range(N)]
moveCnt = [[0] * N for _ in range(N)]
cmd = [[None] * N for _ in range(N)]
for i in range(N):
	for j in range(N):
		s, c = order[i][j][:-1], order[i][j][-1]
		moveCnt[i][j] = int(s)
		cmd[i][j] = directions[c]

def playGame(cx, cy, N):
	x, y = cx, cy
	visited = [[False] * N for _ in range(N)]
	visited[x][y] = True
	
	result = 1
	flag = True
	while flag:
		mx, my = cmd[x][y]
		for _ in range(moveCnt[x][y]):
			x, y = (x + mx) % N, (y + my) % N
			
			if visited[x][y]:
				flag = False
				break
			visited[x][y] = True
			result += 1
	return result


goormScore = playGame(Rg, Cg, N)
playerScore = playGame(Rp, Cp, N)

if goormScore > playerScore:
	print("goorm", goormScore)
else:
	print("player", playerScore)
		