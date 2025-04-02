def solution(k, score):
    answer = []
    honor = [];
    for i in range(len(score)):
        if len(honor) < k:
            honor.append(score[i])
        else:
            if min(honor) < score[i]:
                del honor[-1]
                honor.append(score[i])
                
        honor.sort(reverse=True)
        answer.append(honor[-1])
    return answer