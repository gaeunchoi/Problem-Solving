def solution(n, build_frame):
    built = set()
    
    def valid():
        for x, y, a in built:
            # 기둥일 때
            if a == 0:
                if y == 0 or (x, y-1, 0) in built or (x-1, y, 1) in built or (x, y, 1) in built:
                    continue
                return False
            # 보일 때
            else:
                if (x, y-1, 0) in built or (x+1, y-1, 0) in built or ((x-1, y, 1) in built and (x+1, y, 1) in built):
                    continue
                return False
        return True
    
    for x, y, a, b in build_frame:
        if b == 1:
            built.add((x, y, a))
            if not valid():
                built.remove((x, y, a))
        else:
            if (x, y, a) in built:
                built.remove((x, y, a))
                if not valid():
                    built.add((x, y, a))
                    
    return sorted(built, key = lambda x: (x[0], x[1], x[2]))