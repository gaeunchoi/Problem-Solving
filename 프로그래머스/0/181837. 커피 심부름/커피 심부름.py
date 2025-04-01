def solution(order):
    answer = 0

    for ele in order:
        if 'cafelatte' in ele:
            answer += 5000
        else:
            answer += 4500
    
    return answer