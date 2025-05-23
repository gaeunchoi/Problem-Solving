def solution(n):
    MOD = 1000000007
    a, b = 1, 2
    if n == 1:
        return a
    if n == 2:
        return b
    
    for i in range(3, n + 1):
        a, b = b, (a + b) % MOD
    
    return b