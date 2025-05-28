from collections import deque
def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(q1)
    sum2 = sum(q2)
    total = sum1 + sum2
    
    if total % 2 != 0:
        return -1
    
    target = total // 2
    cnt = 0
    max_cnt = len(queue1) * 3
    
    while cnt <= max_cnt:
        if sum1 == target:
            return cnt
        if sum1 > target:
            moveNum = q1.popleft()
            sum1 -= moveNum
            q2.append(moveNum)
            sum2 += moveNum
        else:
            moveNum = q2.popleft()
            sum2 -= moveNum
            q1.append(moveNum)
            sum1 += moveNum
        cnt += 1
    return -1