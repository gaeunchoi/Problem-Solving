from itertools import permutations
def solution(k, dungeons):
    result = 0
    for permu in permutations(dungeons, len(dungeons)):
        cur_tired = k
        cnt = 0
        for min_need, cost in permu:
            if cur_tired >= min_need:
                cur_tired -= cost
                cnt += 1
        result = max(result, cnt)
    return result