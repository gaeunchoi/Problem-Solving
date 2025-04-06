def count_divisor(n):
    cnt = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            cnt += 1 if i == n // i else 2
    return cnt
    
def solution(number, limit, power):
    result = 0
    for i in range(1, number + 1):
        divisor = count_divisor(i)
        result += power if divisor > limit else divisor
    return result