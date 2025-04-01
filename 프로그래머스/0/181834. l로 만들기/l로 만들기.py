def solution(myString):
    answer = ''
    for ms in myString:
        answer += 'l' if ord(ms) < ord('l') else ms
    return answer