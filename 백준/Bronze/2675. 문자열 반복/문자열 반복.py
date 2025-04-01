T = int(input())

for i in range(T):
    r, str = input().split()

    result = ""

    for j in str:
        result += int(r) * j

    print(result)
