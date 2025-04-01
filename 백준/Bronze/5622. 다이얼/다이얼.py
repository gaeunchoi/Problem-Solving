str = list(input())
list = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
total = 0

for i in str:
    for j in list:
        if i in j:
            total += (3 + list.index(j))

print(total)