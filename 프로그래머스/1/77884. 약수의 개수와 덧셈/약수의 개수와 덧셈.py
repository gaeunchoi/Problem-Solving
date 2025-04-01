

# 제곱수 => 약수의 개수가 홀수개
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        answer += -i if int(i**0.5) == i**0.5 else i
    return answer