def solution(clothes):
    clothesMap = {}
    for item, type in clothes:
        if type not in clothesMap:
            clothesMap[type] = 0
        clothesMap[type] += 1
    
    combinations = 1
    for val in clothesMap.values():
        combinations *= (val + 1)
    
    return combinations-1
        
        