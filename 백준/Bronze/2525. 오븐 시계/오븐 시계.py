import sys

A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline().rstrip())

B = B + C

if B >= 60:
    A += B // 60
    B = B % 60

if A >= 24:
    A -= 24
    
print(A, B)