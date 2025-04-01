def solution(d, budget):
    d.sort()
    answer = 0
    cnt = 0
    for i in range(len(d)):
        answer += d[i]
        if answer > budget:
            return cnt
        cnt += 1
    return cnt