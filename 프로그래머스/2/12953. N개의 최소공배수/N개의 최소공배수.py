def GCD(a, b):
    while b:
        a, b = b, a % b
    return a

def LCM(a, b):
    result = (a * b) // GCD(a, b)
    return result

def solution(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result = LCM(result, arr[i])
    return result
    