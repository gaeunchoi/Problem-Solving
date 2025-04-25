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

    result = ''.join(sorted(common, reverse=True))

    return "0" if result[0] == '0' else result
