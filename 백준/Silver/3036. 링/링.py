import sys
from math import gcd

def yakboon(bunja, bunmo):
    frac = [bunja, bunmo]

    frac_gcd = gcd(frac[0], frac[1])

    frac[0] = frac[0] / frac_gcd
    frac[1] = frac[1] / frac_gcd
    
    return frac

N = int(input())

Rs = list(map(int, sys.stdin.readline().split()))


for i in range(1, N):
    frac = list(yakboon(Rs[i], Rs[0]))
    print('%d/%d' % (frac[1], frac[0]))