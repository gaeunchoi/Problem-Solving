from collections import deque
def is_one_letter_diff(a, b):
    cnt = 0
    for x, y in zip(a, b):
        if x != y:
            cnt += 1
    return cnt == 1

def solution(begin, target, words):
    visited = set([begin])
    q = deque([[begin, 0]])
    
    while q:
        cur, step = q.popleft()
        if cur == target:
            return step
        for word in words:
            if is_one_letter_diff(word, cur) and word not in visited:
                visited.add(word)
                q.append([word, step+1])
    return 0