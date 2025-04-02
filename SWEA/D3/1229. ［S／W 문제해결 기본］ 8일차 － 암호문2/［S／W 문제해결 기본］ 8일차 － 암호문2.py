for tc in range(1, 11):
    len_origin = int(input())
    origin = list(map(int, input().split()))
    len_order = int(input())
    order = list(map(str, input().split()))

    i = 0
    for _ in range(len_order):
        ID, x, y = order[i], order[i + 1], order[i + 2]
        if ID == 'I':
            for j in range(int(y)):
                origin.insert(int(x)+j, order[i+3+j])
            i = i + 3 + int(y)
        else:
            del origin[int(x) : int(x) + int(y)]
            i = i + 3


    print(f'#{tc}', end = ' ')
    for i in range(10):
        print(origin[i], end = ' ')
    print()