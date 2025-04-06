def count_prime(n):
    if n < 2:
        return 0
    
    result = [True] * (n+1)
    result[0] = result[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if result[i]:
            for j in range(i*i, n+1, i):
                result[j] = False
    return sum(result)

def solution(n):
    return count_prime(n)