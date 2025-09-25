def solution(s):
    if len(s) == 1:
        return 1

    answer = len(s)
    for idx in range(1, len(s) // 2 + 1):
        result = ''
        prev = s[:idx]
        count = 1
        for i in range(idx, len(s), idx):
            cur = s[i : i + idx]
            if cur == prev:
                count += 1
            else:
                result += (str(count) + prev if count > 1 else prev)
                prev = cur
                count = 1

        result += (str(count) + prev if count > 1 else prev)
        answer = min(answer, len(result))
    return answer