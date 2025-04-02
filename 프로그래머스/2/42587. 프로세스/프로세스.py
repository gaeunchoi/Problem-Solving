from collections import deque
def solution(priorities, location):
    queue = deque((idx, pro) for idx, pro in enumerate(priorities))
    answer = 0

    while True:
        current = queue.popleft()
        if any(current[1] < q[1] for q in queue):
            queue.append(current)
        else:
            answer += 1
            if current[0] == location:
                return answer