import sys

num = sys.stdin.readline().rstrip()

list = []

for i in str(num):
    list.append(int(i))

list.sort(reverse=True)

for i in list:
    print(i, end="")