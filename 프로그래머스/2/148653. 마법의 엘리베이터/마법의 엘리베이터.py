def solution(storey):
    result = 0
    
    while storey:
        res = storey % 10
        
        if 5 < res:
            result += (10 - res)
            storey += 10
        elif res <= 4:
            result += res
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            result += res
        storey //= 10
    
    return result
            
            