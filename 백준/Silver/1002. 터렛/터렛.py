import math

T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dis = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    # 두 원이 일치하는 경우
    if dis == 0 and r1 == r2 :
        print(-1)
    # 두 원이 한 점에서 만나는 경우(외접 & 내접)
    elif abs(r1 - r2) == dis or r1 + r2 == dis :
        print(1)
    # 두 원이 두 점에서 만나는 경우
    elif abs(r1 - r2) < dis < (r1 + r2) :
        print(2)
    # 두 원이 만나지 않는 경우
    else :
        print(0)