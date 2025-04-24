def solution(s):
    cnt = 0
    x = []
    not_x = []
    for c in s:
        if not x:
            x.append(c)
        else:
            if c == x[0]:
                x.append(c)
            else:
                not_x.append(c)
        
        if(len(x) == len(not_x)):
            cnt += 1
            x = []
            not_x = []
            
    if x or not_x:
        cnt += 1
    
    return cnt