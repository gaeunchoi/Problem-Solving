from itertools import permutations
def solution(k, dungeons):
    permu_dungeons = permutations(dungeons, len(dungeons))
    max_cnt = 0
    for permu in permu_dungeons:
        cur_tired = k
        cnt = 0
        for min_need, waste in permu:
            if cur_tired < min_need:
                break
            cur_tired -= waste
            cnt += 1
        max_cnt = max(max_cnt, cnt)
    return max_cnt
            