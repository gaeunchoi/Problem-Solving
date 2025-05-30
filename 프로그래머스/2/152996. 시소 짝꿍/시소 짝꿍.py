from collections import Counter
def solution(weights):
    result = 0
    ratios = [1/2, 2/3, 3/4]
    count_dict = Counter(weights)
    weights = list(set(weights))
    
    for k, v in count_dict.items():
        if v > 1:
            result += v * (v-1) / 2
    
    for w in weights:
        for r in ratios:
            combi_num = count_dict[w * r]
            result += combi_num * count_dict[w]
    return result
