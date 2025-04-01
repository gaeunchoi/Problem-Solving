T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())

    human = [i for i in range(1, n+1)]

    for x in range(k):
        for y in range(1, n):
            human[y] += human[y-1]

    print(human[-1])