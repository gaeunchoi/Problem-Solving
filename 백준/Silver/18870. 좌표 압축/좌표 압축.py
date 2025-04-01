import sys

N = int(sys.stdin.readline())

cor = list(map(int, sys.stdin.readline().split()))

sorted_cor = sorted(list(set(cor)))

dic = {sorted_cor[i] : i for i in range(len(sorted_cor))}

for i in cor:
    print(dic[i], end = ' ')

