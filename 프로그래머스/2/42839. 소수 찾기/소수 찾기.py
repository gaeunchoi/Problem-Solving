from itertools import permutations

def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):
        for j in permutations(list(numbers), i):
            permu_num = int(''.join(j))

            for k in range(2, int(permu_num**0.5)+1):
                if permu_num % k == 0:
                    break
            else:
                if permu_num not in answer and permu_num >= 2:
                  answer.append(permu_num)
    return len(answer)
