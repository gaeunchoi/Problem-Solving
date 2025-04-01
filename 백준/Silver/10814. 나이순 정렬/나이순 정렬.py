import sys

N = int(sys.stdin.readline())
users = []

for _ in range(N):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    users.append([age, name])

users.sort(key = lambda x : x[0])

for i in users:
    print(i[0], i[1])