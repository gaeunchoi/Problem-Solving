k = int(input())

arr = [list(map(int, input().split())) for _ in range(6)]

min_w =  min_h = max_w = max_h = 0
maxw_idx = maxh_idx = 0

for idx, tmp in enumerate(arr):
    if tmp[0] == 1 or tmp[0] == 2:
        if max_w < tmp[1]:
            maxw_idx = idx
            max_w = tmp[1]

    elif tmp[0] == 3 or tmp[0] == 4:
        if max_h < tmp[1]:
            maxh_idx = idx
            max_h = tmp[1]

min_h = abs(arr[(maxw_idx - 1) % 6][1] - arr[(maxw_idx + 1) % 6][1])
min_w = abs(arr[(maxh_idx - 1) % 6][1] - arr[(maxh_idx + 1) % 6][1])

print (k * ((max_w * max_h) - (min_w * min_h)))