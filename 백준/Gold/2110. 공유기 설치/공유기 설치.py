n, c = map(int, input().split())
home = [int(input()) for _ in range(n)]
home.sort()

start, end = 1, home[-1] - home[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    current = home[0]
    wifi = 1

    for i in range(n):
        # 다음 집에서 현재 집의 거리가 mid보다 크면 공유기 설치
        if home[i] - current >= mid:
            wifi += 1
            current = home[i]

    if wifi >= c:    # 공유기 설치를 더해야함 -> 간격을 짧게
        result = mid
        start = mid + 1
    else:           # 공유기 설치 완료 / 더 많이 -> 간격을 넓게
         end = mid - 1

print(result)