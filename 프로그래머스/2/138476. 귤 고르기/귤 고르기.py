from collections import Counter
def solution(k, tangerine):
    counter = Counter(tangerine)
    cnts = sorted(counter.values(), reverse = True)
    
    total = 0
    result = 0
    for cnt in cnts:
        total += cnt
        result += 1
        if total >= k:
            break
    return result