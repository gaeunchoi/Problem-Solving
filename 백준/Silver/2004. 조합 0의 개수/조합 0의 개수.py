N, K = map(int, input().split())

# 끝자리가 0이라는 것은 10의 배수
# 10은 2와 5로 구성되어 있음
# 2와 5 짝이 맞아야 10이 되므로 2의 개수와 5의 개수중 더 작은게 10의 개수이다.

def count_number(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count

five_count = count_number(N, 5) - count_number(K, 5) - count_number(N - K, 5)
two_count = count_number(N, 2) - count_number(K, 2) - count_number(N - K, 2)

answer = min(five_count, two_count)
print(answer)