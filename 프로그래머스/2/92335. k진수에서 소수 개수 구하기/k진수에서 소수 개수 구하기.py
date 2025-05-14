def is_Prime(n):
    if n <= 2 or n % 2 == 0:
        return n == 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
    
def convert_Num(n, k):
    convert_num = ""
    while n > 0:
        convert_num = str(n % k) + convert_num
        n //= k
    return convert_num
    
def solution(n, k):
    candidates = convert_Num(n, k).split("0")
    
    result = 0
    for cand in candidates:
        if cand and is_Prime(int(cand)):
            result += 1
    return result