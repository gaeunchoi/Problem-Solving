from collections import deque

# queue를 이용하자.
# 현재 가격 === 큐의 맨 앞 원소를 추출하고, 반복문을 돌면서 큐 안의 원소보다 크다면 t++
# 현재 가격이 큐 안의 원소보다 작다면 break로 탈출(가격이 줄어든것)
def solution(prices):
    answer = []
    prices = deque(prices)

    while prices:
        p = prices.popleft()
        t = 0
        for val in prices:
             t += 1
             if p > val:
                 break
        answer.append(t)
    return answer