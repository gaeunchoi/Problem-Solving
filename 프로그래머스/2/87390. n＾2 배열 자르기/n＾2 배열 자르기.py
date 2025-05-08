def solution(n, left, right):
    n_pow_arr = []
    for i in range(left, right + 1):
        n_pow_arr.append(max(i // n, i % n) + 1)
    return n_pow_arr