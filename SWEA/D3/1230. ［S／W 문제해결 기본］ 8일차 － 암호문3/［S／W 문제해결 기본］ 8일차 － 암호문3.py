for tc in range(1, 11):
    len_origin = int(input())
    origin = list(map(int, input().split()))
    len_order = int(input())
    order = list(map(str, input().split()))

    i = 0
    for _ in range(len_order):
        IDA = order[i]
        if IDA == 'I':
            x, y = int(order[i+1]), int(order[i+2])
            for j in range(y):
                origin.insert(x+j, order[i+3+j])
            i = i + 3 + y
        elif IDA == 'D':
            x, y = int(order[i + 1]), int(order[i + 2])
            del origin[x : x + y]
            i = i + 3
        elif IDA == 'A':
            y = int(order[i + 1])
            origin.extend(order[i + 2 : i + 2 + y])
            i = i + 2 + y

    print(f'#{tc}', end = ' ')
    print(*origin[:10])