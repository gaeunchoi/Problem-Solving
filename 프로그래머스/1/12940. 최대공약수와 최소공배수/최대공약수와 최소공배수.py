def GCD(a, b):
    while b:
        a, b = b, a%b
    return a

def LCM(a, b):
    return (a*b) // GCD(a, b)

def solution(n, m):
    return [GCD(n, m), LCM(n, m)]