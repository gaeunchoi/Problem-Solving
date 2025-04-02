def solution(a, b, n):
    result = 0
    while n >= a:
        ret, res = divmod(n, a)
        result += ret*b
        n = ret*b + res
    return result