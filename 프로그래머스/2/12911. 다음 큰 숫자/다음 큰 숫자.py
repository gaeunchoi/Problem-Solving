def solution(n):
    n_one_cnt = bin(n)[2:].count("1")
    target = n + 1
    while True:
        if bin(target)[2:].count("1") == n_one_cnt:
            return target
        target += 1