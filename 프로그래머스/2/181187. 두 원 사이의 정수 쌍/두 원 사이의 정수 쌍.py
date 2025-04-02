import math

def solution(r1, r2):
    quarter = 0

    pr1, pr2 = r1 ** 2, r2 ** 2
    for i in range(1, r2+1):
        s = math.ceil(math.sqrt(pr1 - i ** 2)) if i < r1 else 0
        
        e = int(math.sqrt(pr2 - i ** 2))
        quarter += e - s + 1

    return 4 * quarter