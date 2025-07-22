def solution(n):
    result = ''
    while n > 0:
        a, b = divmod(n, 3)
        if b == 0:
            result = '4' + result
            n = a - 1
        else:
            result = str(b) + result
            n = a
    return result