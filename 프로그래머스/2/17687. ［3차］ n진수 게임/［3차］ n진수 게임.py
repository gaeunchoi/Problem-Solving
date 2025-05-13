def convert(num, base):
    digits = "0123456789ABCDEF"
    
    if num == 0:
        return "0"
    
    result = ""
    while num > 0:
        result = digits[num % base] + result
        num //= base
    return result

def solution(n, t, m, p):
    result = ""
    full_string = ""
    number = 0
    
    while len(full_string) < t * m:
        full_string += convert(number, n)
        number += 1

    for i in range(t):
        result += full_string[i * m + (p - 1)]

    return result