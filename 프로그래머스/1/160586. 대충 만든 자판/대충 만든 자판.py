def solution(keymap, targets):
    first_appear = {}
    for mapping in keymap:
        for idx, k in enumerate(mapping):
            if k not in first_appear:
                first_appear[k] = idx+1
            else:
                first_appear[k] = min(first_appear[k], idx+1)

    result = []
    for target in targets:
        cnt = 0
        for t in target:
            if t not in first_appear:
                cnt = -1
                break
            cnt += first_appear[t]
        result.append(cnt)
    
    return result