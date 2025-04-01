def solution(food):
    answer = ''
    for idx in range(1, len(food)):
        answer += str(idx) * (food[idx] // 2)
    return answer + "0" + answer[::-1]