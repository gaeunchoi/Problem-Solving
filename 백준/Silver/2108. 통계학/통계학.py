import sys
from collections import Counter

N = int(sys.stdin.readline())

nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))

nums.sort()

# 산술평균
print(round(sum(nums)/N))

# 중앙값
print(nums[N//2])

# 최빈값
numss = Counter(nums).most_common()

if len(numss) > 1:
    if numss[0][1] == numss[1][1]:
        print(numss[1][0])
    else:
        print(numss[0][0])
else:
    print(numss[0][0])

# 범위
print(nums[-1] - nums[0])