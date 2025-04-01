def solution(n, lost, reserve):
    lost, reserve = set(lost), set(reserve)
    reserve_s, lost_s = set(reserve) - set(lost), set(lost) - set(reserve)

    for extra in sorted(reserve_s):
        if extra-1 in lost_s:
           lost_s.remove(extra-1)
        elif extra+1 in lost_s:
           lost_s.remove(extra+1)

    return n - len(lost_s)