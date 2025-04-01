def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1, arr2):
        row = str(bin(i|j)[2:])
        row = row.rjust(n, '0')
        row = row.replace('1', '#').replace('0', ' ')
        answer.append(row)
    return answer