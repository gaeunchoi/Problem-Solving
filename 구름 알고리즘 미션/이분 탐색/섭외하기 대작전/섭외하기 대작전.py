import sys
input = sys.stdin.readline
from bisect import bisect

N = int(input())
S = sorted(map(int, input().split()))

answer = 0
for i in range(N-2):
	for j in range(i+1, N-1):
		idx = bisect(S, S[i] + S[j]) - 1
		answer += idx - j
print(answer)