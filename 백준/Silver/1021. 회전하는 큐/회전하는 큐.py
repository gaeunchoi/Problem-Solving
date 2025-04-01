from collections import deque

n, m = map(int, input().split())
num = list(map(int, input().split()))

arr = deque([i for i in range(1, 1+n)])
cnt = 0

for i in num:
    while True:
        if arr[0] == i:
            arr.popleft()
            break
        else:
            if arr.index(i) <= len(arr)//2 :
                arr.rotate(-1)
            else:
                arr.rotate(1)
            cnt += 1

print(cnt)