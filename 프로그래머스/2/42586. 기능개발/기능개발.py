from math import ceil

def solution(progresses, speeds):
    answer = []
    days = []
    front = 0

    # 소요시간을 정리해두자
    for i in range(len(progresses)):
        days.append(ceil((100 - progresses[i]) / speeds[i]))
    
    for idx in range(len(days)):
        if days[idx] > days[front]:
            answer.append(idx - front)
            front = idx
    answer.append(len(days) - front)

    return answer