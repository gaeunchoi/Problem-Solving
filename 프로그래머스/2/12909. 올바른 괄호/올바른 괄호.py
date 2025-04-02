def solution(s):
    stack = []
    for i in s:
        if i == '(':          # '('인 경우 스택에 추가
            stack.append(i)
        else:                 # ')'인 경우
            if not stack:     # 괄호 짝이 안맞는다면 -> ')(' 인 경우
                return False
            stack.pop()       # 괄호 짝이 맞는다면 -> '()'인 경우

    if stack:
        return False
    return True