from collections import Counter
def solution(N, stages):
    stages_cnt = Counter(stages)

    result = []
    acc = 0
    total = len(stages)
    for i in range(1, N+1):
        if total - acc == 0:
            fail_rate = 0
        else:
            fail_rate = stages_cnt[i] / (total - acc)
        acc += stages_cnt[i]
        result.append([fail_rate, i])
        
    answer = [row[1] for row in sorted(result, key = lambda x: x[0], reverse=True)]
    return answer

        