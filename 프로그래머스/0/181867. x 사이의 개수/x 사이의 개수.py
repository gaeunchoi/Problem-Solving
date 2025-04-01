def solution(myString):
    string = list(map(str, myString.split("x")))
    answer = [len(x) for x in string]
    return answer