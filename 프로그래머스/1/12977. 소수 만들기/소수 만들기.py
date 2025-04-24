from itertools import combinations
def isPrime(a, b, c):
    n = a + b + c
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    combi_nums = combinations(nums, 3)
    cnt = 0
    for a, b, c in combi_nums:
        if isPrime(a, b, c):
            cnt += 1
            
    return cnt
    