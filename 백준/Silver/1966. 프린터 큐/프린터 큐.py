T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    importance = list(map(int, input().split()))
    pos = [0 for _ in range(n)]
    pos[m] = 1

    cnt = 0
    while True:
        if importance[0] == max(importance):
            cnt += 1

            if pos[0] != 1:
                del importance[0]
                del pos[0]
            else:
                print(cnt)
                break

        else:
            importance.append(importance[0])
            pos.append(pos[0])
            del importance[0]
            del pos[0]

