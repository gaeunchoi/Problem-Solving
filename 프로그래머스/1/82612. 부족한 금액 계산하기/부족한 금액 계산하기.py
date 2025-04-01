def solution(price, money, count):
    answer = 0
    for i in range(count):
        answer += price * (i+1)
    return answer-money if answer > money else 0