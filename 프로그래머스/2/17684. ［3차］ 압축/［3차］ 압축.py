def solution(msg):
    result = []
    alpha_dict = {chr(64 + i): i for i in range(1, 27)}
    
    s = e = 0
    while True:
        e += 1
        if e == len(msg):
            result.append((alpha_dict[msg[s : e]]))
            break
        
        if msg[s : e+1] not in alpha_dict:
            alpha_dict[msg[s : e+1]] = len(alpha_dict) + 1
            result.append(alpha_dict[msg[s:e]])
            s = e
    return result
            