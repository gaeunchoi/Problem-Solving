# 짝수 => f(x) = x + 1
# 홀수 => x 가장 오른쪽 "01"을 "10"으로 바꾸기
def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
        else:
            bin_num = list("0" + bin(num)[2:]) 
            idx = ''.join(bin_num).rfind("01") 
            bin_num[idx] = '1'
            bin_num[idx + 1] = '0'
            answer.append(int(''.join(bin_num), 2))
    return answer