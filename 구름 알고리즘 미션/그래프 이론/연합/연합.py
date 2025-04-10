import sys
input = sys.stdin.readline
from collections import deque


N, M = map(int, input().split())
connection = [[False] * (N+1) for _ in range(N+1)]

for _ in range(M):
	s, e = map(int, input().split())
	connection[s][e] = True
	
graph = [[] for _ in range(N+1)]
for i in range(1, N):
	for j in range(i+1, N+1):
		if connection[i][j] and connection[j][i]:
			graph[i].append(j)
			graph[j].append(i)
			
visited = [False] * (N+1)
result = 0

for i in range(1, N+1):
	if not visited[i]:
		result += 1
		q = deque([i])
		visited[i] = True
		
		while q:
			val = q.popleft()
			for next in graph[val]:
				if not visited[next]:
					q.append(next)
					visited[next] = True
print(result)