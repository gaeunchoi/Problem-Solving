sticks = list(map(int, input().split()))
sticks.sort()
a, b, c = sticks

if a + b <= c:
    c = a + b -1

print(a+b+c)