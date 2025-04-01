def solution(q, r, code):
    answer = ''
    for i, value in enumerate(code):
        if i % q == r:
            answer += value
    return answer