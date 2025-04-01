def solution(arr):
    answer = [arr[0]]
    for ele in arr:
        if answer[-1] != ele:
            answer.append(ele)
        else:
            continue
    return answer
