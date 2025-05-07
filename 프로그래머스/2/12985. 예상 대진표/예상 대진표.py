import math

def ceil(num):
    return math.ceil(num / 2)

def solution(n,a,b):
    result = 1
    
    while ceil(a) != ceil(b):
        a = ceil(a)
        b = ceil(b)
        result += 1
    return result