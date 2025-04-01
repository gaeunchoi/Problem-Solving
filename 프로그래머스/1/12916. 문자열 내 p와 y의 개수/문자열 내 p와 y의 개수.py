def solution(s):
    isP = isY = 0
    for ele in s:
        if ele == 'P' or ele == 'p':
            isP += 1
        if ele == 'Y' or ele == 'y':
            isY += 1
    return True if isP == isY else False