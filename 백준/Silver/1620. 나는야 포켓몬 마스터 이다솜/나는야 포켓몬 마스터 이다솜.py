import sys


N, M = map(int, input().split())
pocketmon = {}
pocketmon_num = {}

for i in range(N):
    name = sys.stdin.readline().rstrip()
    pocketmon[name] = i+1
    pocketmon_num[i+1] = name

for i in range(M):
    order = sys.stdin.readline().rstrip()

    if order in pocketmon.keys():
        print(pocketmon[order])
    else:
        print(pocketmon_num[int(order)])
    
