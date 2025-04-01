def solution(arr, divisor):
    result = sorted(list(v for v in arr if v % divisor == 0))
    return result if len(result) != 0 else [-1]