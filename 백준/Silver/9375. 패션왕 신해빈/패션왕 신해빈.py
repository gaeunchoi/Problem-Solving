T = int(input())

for _ in range(T):
    n = int(input())

    if n == 0:
        print(0)
        continue
        
    wearable = dict()
    for _ in range(n):
        wear_name, wear_type = map(str, input().split())

        if wear_type in wearable.keys():
            wearable[wear_type] += 1
        else:
            wearable[wear_type] = 1

        result = 1
        for key in wearable.keys():
            result *= wearable[key] + 1

    print(result - 1)




