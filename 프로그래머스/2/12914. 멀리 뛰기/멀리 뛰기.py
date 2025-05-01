from math import factorial

def solution(n):
    result = 0
    for i in range(n // 2 + 1):
        cnt_one = n - 2 * i
        cnt_total = cnt_one + i
        result += (factorial(cnt_total) // (factorial(cnt_one) * factorial(i))) % 1234567
    return result % 1234567
        
    