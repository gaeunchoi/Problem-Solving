import sys
from math import sqrt

def isPrime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

T = int(input())
for i in range(T):
    n = int(sys.stdin.readline().rstrip()) 
    while True:
        if isPrime(n):
            print(n)
            break
        else:
            n += 1