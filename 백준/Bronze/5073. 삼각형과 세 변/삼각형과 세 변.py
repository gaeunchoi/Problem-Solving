while True:
    a, b, c = map(int, input().split())
    if a == b == c:
        if a == 0:
            break
        else:
            print('Equilateral')
    elif a == b or b == c or c == a:
        if max([a, b, c]) >= sum([a, b, c]) - max([a, b, c]):
            print('Invalid')
        else:
            print('Isosceles')
    else:
        if max([a, b, c]) >= sum([a, b, c]) - max([a, b, c]):
            print('Invalid')
        else:
            print('Scalene')