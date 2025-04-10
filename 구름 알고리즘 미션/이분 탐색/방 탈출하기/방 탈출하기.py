import sys
input = sys.stdin.readline
from bisect import bisect

N = int(input())
A = sorted(map(int, input().split()))
M = int(input())
B = [int(input()) for _ in range(M)]


for i in range(M):
	j = bisect(A, B[i])
	print(1 if j and A[j-1] == B[i] else 0)