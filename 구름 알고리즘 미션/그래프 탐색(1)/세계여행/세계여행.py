import sys
input = sys.stdin.readline
from collections import deque

def bfs(language):
	q = deque()
	q.append(0)
	visited = [False] * N
	visited[0] = True
	
	while q:
		country = q.popleft()
		for oc in graph[country]:
			if not visited[oc] and (a[oc] == a[0] or a[oc] == language):
				visited[oc] = True
				q.append(oc)
	
	visitCnt = 0
	for i in range(N):
		if visited[i]:
			visitCnt += 1
	return visitCnt


N, M = map(int, input().split())
a = list(map(int, input().split()))

graph = [[] for _ in range(N)]
for _ in range(M):
	p, q = map(int, input().split())
	graph[p-1].append(q-1)
	graph[q-1].append(p-1)
	
result = 0
for i in range(1, 11):
	if a[0] != i:
		result = max(result, bfs(i))
		
print(result)