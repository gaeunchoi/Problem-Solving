def solution(picture, k):
    answer = []
    for row in picture:
        tmp = ''
        for pixel in row:
            tmp += pixel * k
        for _ in range(k):
            answer.append(tmp)
    return answer