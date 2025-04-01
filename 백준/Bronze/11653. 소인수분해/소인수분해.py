N = int(input())
pivot = 2

while pivot <= N:
    if N % pivot == 0:
        print(pivot)
        N = N / pivot
    else:
        pivot += 1

