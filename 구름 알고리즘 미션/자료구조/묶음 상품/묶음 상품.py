import sys
input = sys.stdin.readline

def find(u):
	if parent[u] != u:
		parent[u] = find(parent[u])
	return parent[u]

def union(u, v):
	root_u = find(u)
	root_v = find(v)
	
	if root_u == root_v:
		return False
	
	if root_u < root_v:
		parent[root_v] = root_u
	else:
		parent[root_u] = root_v
	return True

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
cnt = N
for _ in range(M):
	a, b = map(int, input().split())
	if union(a, b):
		cnt -= 1
		
print(cnt)