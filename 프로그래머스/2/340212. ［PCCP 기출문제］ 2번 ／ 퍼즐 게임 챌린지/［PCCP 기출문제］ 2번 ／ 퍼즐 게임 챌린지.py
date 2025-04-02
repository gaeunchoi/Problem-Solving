def solve_puzzle(level, diffs, times):
    solve_time = 0
    for i in range(len(diffs)):
        if diffs[i] <= level:
            solve_time += times[i]
        else:
            solve_time += (diffs[i] - level) * (times[i] + times[i-1]) + times[i]

    return solve_time


def solution(diffs, times, limit):
    level_arr = [i for i in range(min(diffs), max(diffs)+1)]

    # binary_search(level_arr, 0, len(level_arr)-1, diffs, times, limit)
    start, end = 0, len(level_arr)-1

    levelable = []
    while start <= end:
        pivot = (start + end) // 2

        if solve_puzzle(level_arr[pivot], diffs, times) <= limit:
            levelable.append(level_arr[pivot])
            end = pivot - 1
        else:
            start = pivot + 1

    answer = min(levelable)

    return answer