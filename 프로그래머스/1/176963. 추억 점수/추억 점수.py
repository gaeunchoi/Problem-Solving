def solution(name, yearning, photo):
    answer = [0] * len(photo)
    scores = {}
    for i in range(len(name)):
        scores[name[i]] = yearning[i]
    
    for i in range(len(photo)):
        for j in photo[i]:
            answer[i] += scores[j] if j in scores.keys() else 0
        
    return answer