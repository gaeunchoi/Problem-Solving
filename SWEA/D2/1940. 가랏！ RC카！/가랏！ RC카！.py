T = int(input())

for tc in range(1, T+1):
    distance = 0
    speed = 0
    N = int(input())
    for _ in range(N):
        command = list(input().split())
        if int(command[0]) == 1:
            speed += int(command[1])
        elif int(command[0]) == 2:
            speed -= int(command[1])
            if speed < 0:
                speed = 0
        distance += speed

    print(f'#{tc} {distance}')