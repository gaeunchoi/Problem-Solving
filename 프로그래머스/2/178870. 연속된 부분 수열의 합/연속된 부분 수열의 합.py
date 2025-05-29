def solution(sequence, k):
    n = len(sequence)
    left = total = 0
    result = []
    min_len = float('inf')

    for right in range(n):
        total += sequence[right]

        while total > k:
            total -= sequence[left]
            left += 1

        if total == k:
            if right - left < min_len:
                min_len = right - left
                result = [left, right]

    return result
