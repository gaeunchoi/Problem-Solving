import sys

def cantor(n):
    if n == 1:
        return "-"

    cantor_unit = cantor(n // 3)
    return cantor_unit + " " * (n//3) + cantor_unit

while True:
    try:
        N = int(sys.stdin.readline())
        print(cantor(3**N))
    except:
        break