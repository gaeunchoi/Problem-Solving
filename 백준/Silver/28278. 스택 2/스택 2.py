import sys

N = int(input())
s = []

def is_empty():
    if len(s) == 0:
        return 1

for i in range(N):
    order = sys.stdin.readline().split()

    if order[0] == '1':
        s.append(order[1])
    elif order[0] == '2':
        if s:
            print(s.pop())
        else:
            print(-1)
    elif order[0] == '3':
        print(len(s))
    elif order[0] == '4':
        emp = 1 if is_empty() == 1 else 0
        print(emp)
    else:
        if s:
            print(s[-1])
        else:
            print(-1)