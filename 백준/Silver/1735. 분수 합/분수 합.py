frac1 = list(map(int, input().split()))
frac2 = list(map(int, input().split()))

def GCD(a, b):
    while b:
        a, b = b, a % b
    return a
    
def LCM(a, b):
    result = (a * b) // GCD(a, b)
    return result

down = LCM(frac1[1], frac2[1])
up = frac1[0] * (down // frac1[1]) + frac2[0] * (down // frac2[1])

tmp = GCD(up, down)
if tmp != 1:
    up, down = up // tmp, down // tmp

print(up, down)