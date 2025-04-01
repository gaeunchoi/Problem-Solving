def solution(today, terms, privacies):
    answer = []
    ty, tm, td = map(int, today.split('.'))
    expiration = {}

    for term in terms:
        t, m = term.split()
        expiration[t] = int(m) * 28

    for i in range(len(privacies)):
        date, type = privacies[i].split()
        dy, dm, dd = map(int, date.split('.'))
        y, m, d = ty - dy, tm - dm, td - dd

        total = y * 336 + m * 28 + d
        if expiration[type] <= total:
            answer.append(i+1)

    return answer