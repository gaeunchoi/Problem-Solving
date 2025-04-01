def solution(s):
    answer = []
    for idx, c in enumerate(s):
        nearIdx = s.rfind(c, 0, idx)
        answer.append(-1 if nearIdx < 0 else idx - nearIdx)
    return answer