from collections import Counter
def solution(wants, number, discount):
    result = 0
    total_days = len(discount)
    
    for i in range(total_days - 9):
        want_cnt = Counter(discount[i : i + 10])
        
        success = True
        for want, num in zip(wants, number):
            if want_cnt[want] < num:
                success = False
                break
                
        if success:
            result += 1
            
    return result