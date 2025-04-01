import math

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    dis = b - a
    cum_dis = 1
    cnt = 1

    while cum_dis < dis:
        cum_dis += math.ceil(cnt / 2)
        if cum_dis > dis:
            break
        cnt += 1

    print(cnt)