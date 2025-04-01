A, B = map(int, input().split())

def GCD(a, b):
    while b:
        a, b = b, a%b
    return a

def LCM(a, b):
    result = (a*b) // GCD(a, b)
    return result

print(LCM(A, B))