def solution(elements):
    N = len(elements)
    circle_elements = elements * 2
    result = set()
    
    for length in range(1, N+1):
        for start in range(N):
            result.add(sum(circle_elements[start: start+length]))
    return len(result)