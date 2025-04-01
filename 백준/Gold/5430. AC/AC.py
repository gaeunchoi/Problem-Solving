from collections import deque
import sys

T = int(input())

for _ in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    xn = deque(sys.stdin.readline().rstrip()[1:-1].split(","))

    if n == 0 :
        xn = []

    flag = 0
    for i in p:
        if i == 'R':
            flag += 1
        elif i == 'D':
            if len(xn) == 0 :
                print("error")
                flag = 1
                break
            else:
                if flag % 2 == 0:
                    xn.popleft()
                else:
                    xn.pop()

    else:
        if flag % 2 == 1:
            xn.reverse()
        print("[" + ",".join(xn) + "]")