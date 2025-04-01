def solution(data, ext, val_ext, sort_by):
    answer = []
    dict = {"code": 0, "date": 1, "maximum": 2, "remain": 3}

    for element in data:
        ext_value = element[dict[ext]]
        if ext_value <= val_ext:
            answer.append(element)

    answer.sort(key = lambda x: x[dict[sort_by]])
    return answer