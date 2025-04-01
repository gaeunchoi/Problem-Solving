from itertools import combinations
def solution(number):
    answer = 0
    permu_student = list(combinations(number, 3))
    for permu in permu_student:
        if sum(permu) == 0:
            answer += 1
    return answer