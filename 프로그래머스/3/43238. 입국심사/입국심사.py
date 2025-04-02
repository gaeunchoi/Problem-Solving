def solution(n, times):
    low, high = 1, max(times)*n
    answer = high

    while low <= high:
        mid = (low + high) // 2
        total = 0

        for time in times:
            total += mid // time

        if total >= n:
            answer = mid
            high = mid - 1
        else:
            low = mid+1

    return answer