def solution(strArr):
    ans = [0] * 31
    for s in strArr:
        ans[len(s)] += 1
    return max(ans)