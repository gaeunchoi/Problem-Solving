from math import gcd

N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    print(a * b // gcd(a, b))