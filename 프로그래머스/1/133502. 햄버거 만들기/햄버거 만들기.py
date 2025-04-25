def solution(ingredient):
    stack = []
    cnt = 0
    for food in ingredient:
        stack.append(food)
        # 스택의 마지막 4개 요소가 "1231"인지 확인
        if len(stack) >= 4 and "".join(map(str, stack[-4:])) == "1231":
            cnt += 1
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
    return cnt