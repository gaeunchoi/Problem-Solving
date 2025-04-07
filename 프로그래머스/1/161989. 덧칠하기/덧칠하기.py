def solution(n, m, section):
    answer = 0
    idx = 0
    while idx < len(section):
        start = section[idx]
        end = start + m - 1
        answer += 1
        
        while idx < len(section) and section[idx] <= end:
            idx += 1
    return answer