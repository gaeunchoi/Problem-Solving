import sys
import math
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

result = 0
for room in A:
    result += 1
    room -= B
    if room > 0:
        result += math.ceil(room / C)

print(result)