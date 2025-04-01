def solution(my_string, indices):
    answer = [x for x in my_string]
    for i in sorted(indices, reverse=True):
        del answer[i]
    return "".join(answer)