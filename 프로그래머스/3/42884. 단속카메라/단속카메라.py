def solution(routes):
    routes.sort(key=lambda x: x[1])
    
    result = 0
    camera = -30001
    
    for s, e in routes:
        if s > camera:
            camera = e
            result += 1
    
    return result