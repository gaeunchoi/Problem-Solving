def solution(s, skip, index):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    no_skip_alpha = [c for c in alpha if c not in skip]
    
    result = []
    for ch in s:
        i = no_skip_alpha.index(ch)
        shifted_char = no_skip_alpha[(i + index) % len(no_skip_alpha)]
        result.append(shifted_char)
    
    return ''.join(result)