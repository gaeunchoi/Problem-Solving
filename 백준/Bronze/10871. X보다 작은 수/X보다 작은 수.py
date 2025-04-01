a, b = map(int, input().split())

data = list(map(int, input().split()))
for j in data:
    if j < b:
        print(j, end=" ")