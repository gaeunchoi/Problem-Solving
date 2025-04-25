from collections import Counter

def solution(X, Y):
    counter_X = Counter(X)
    counter_Y = Counter(Y)

    common = []
    for digit in map(str, range(10)):
        count = min(counter_X[digit], counter_Y[digit])
        common.extend([digit] * count)

    if not common:
        return "-1"

    common.sort(reverse=True)
    result = ''.join(common)

    if result[0] == '0':  # 모든 숫자가 0이면
        return "0"

    return result
