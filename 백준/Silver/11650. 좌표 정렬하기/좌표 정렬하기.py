N = int(input())

arr = []
for _ in range(N):
    [x, y] = map(int, input().split())
    arr.append([x, y])

sorted_arr = sorted(arr)

for i in range(N):
    print(sorted_arr[i][0], sorted_arr[i][1])