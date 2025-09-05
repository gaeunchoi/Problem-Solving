import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
M = int(input())

blood = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    blood[x].append(y)
    blood[y].append(x)

family = [-1 for _ in range(N + 1)]
family[A] = 0

q = deque([A])
while q:
    cur = q.popleft()
    for nxt in blood[cur]:
        if family[nxt] == -1:
            q.append(nxt)
            family[nxt] = family[cur] + 1

print(family[B])