def solution(s):
    result = 0
    i = 0
    while s != "1":
        remove_zero = s.replace("0", "")
        result += len(s) - len(remove_zero)
        s = bin(len(remove_zero))[2:]
        i += 1
    return [i, result]