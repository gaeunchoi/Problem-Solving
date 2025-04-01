import sys
from math import gcd

N = int(input())

nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))

nums.sort()

# A = X * T + R
# B = Y * T + R
# B - A = (Y - X) * T, B - A가 gcd의 배수임을 의미
re_num = []
for i in range(1, N):
    re_num.append(nums[i] - nums[i-1])

def findGCD(a, b):
    num = b
    div = a
    rest = num % div
    while rest != 0:
        num = div
        div = rest
        rest = num % div
    return div

# nums의 모든 수들의 최대공약수를 구하고,
# 그 중 1을 제외한 모든 약수가 구하는 M
GCD = re_num[0]
for i in range(1, len(re_num)):
    GCD = findGCD(GCD, re_num[i])

result = set()

for i in range(2, int(pow(GCD, 0.5)) + 1):
    if GCD % i == 0:    # 약수 찾기
        result.add(i)
        if GCD // i != i:
            result.add(GCD // i)

result.add(GCD)
print(*sorted(list(result)))

