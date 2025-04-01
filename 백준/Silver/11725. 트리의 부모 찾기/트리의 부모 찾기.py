import sys
from collections import deque

N = int(input())
trees = [[0] for _ in range(N+1)]
parents = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    trees[a].append(b)
    trees[b].append(a)

parents[1] = 0

q = deque()
q.append(1)

while q:
    node = q.popleft()
    for next in trees[node]:
        if parents[next] == 0:
            parents[next] = node
            q.append(next)

for i in range(2, N+1):
    print(parents[i])