import sys
from collections import deque

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

M = int(input())
C = list(map(int, sys.stdin.readline().split()))

q = deque([])
for i in range(N):
    if A[i] == 0:
        q.append(B[i])

for i in range(M):
    q.appendleft(C[i])
    print(q.pop(), end = ' ')