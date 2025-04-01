while True:
    a, b, c = map(int, input().split())

    if a == b == c == 0:
        break

    if pow(a, 2) == pow(b, 2) + pow(c, 2) or pow(b, 2) == pow(a, 2) + pow(c, 2) or pow(c, 2) == pow(a, 2) + pow(b, 2):
        print("right")
    else:
        print("wrong")