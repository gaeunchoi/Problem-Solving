def is_valid(s):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in '([{':
            stack.append(ch)
        else:
            if not stack or stack[-1] != bracket_map[ch]:
                return False
            stack.pop()
    return not stack

def solution(s):
    count = 0
    n = len(s)

    for i in range(n):
        rotated = s[i:] + s[:i]
        if is_valid(rotated):
            count += 1

    return count