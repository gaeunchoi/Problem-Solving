import sys
input = sys.stdin.readline

N, M = map(int, input().split())
connectLine = [[]] * M
connectCnt = [0] * N

for i in range(M):
	A, B = map(int, input().split())
	connectLine[i] = [A, B]
	connectCnt[A-1] += 1
	connectCnt[B-1] += 1
	
result = []
for i in range(M):
	A, B = connectLine[i]
	if connectCnt[A-1] > 1 and connectCnt[B-1] > 1:
		result.append(i+1)

if(len(result)):
	print(*result)
else:
	print(-1)