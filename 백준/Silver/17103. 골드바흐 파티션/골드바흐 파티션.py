import sys

T = int(input())

primes = [True] * 1000001
for i in range(2, 1000001):
    if primes[i] == True:
        for j in range(2*i, 1000001, i):
            primes[j] = False

for _ in range(T):
    result = 0
    
    n = int(sys.stdin.readline().rstrip())
    
    for i in range(2, n // 2 + 1):
        if primes[i] and primes[n - i]:
            # print('두 소수 더해도 돼', i, n-i)
            result += 1
    
    print(result)