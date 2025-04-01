# 숫자 10 처리하려면 점수를 문자열로 이어붙어야함
def solution(dartResult):
    result = []
    score = ''
    for dart in dartResult:
        if dart.isdigit():
            score += dart
        elif dart == 'S':
            result.append(int(score))
            score = ''
        elif dart == 'D':
            result.append(int(score)**2)
            score = ''
        elif dart == 'T':
            result.append(int(score)**3)
            score = ''
        elif dart == '*':
            if len(result) <= 1:
                result[0] *= 2
            else:
                result[-2] *= 2
                result[-1] *= 2
        elif dart == '#':
            result[-1] *= -1
        
    return sum(result)
