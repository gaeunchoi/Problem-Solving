n = int(input())

cnt = 0
stack = []
result = []
tmp = True

for i in range(n):
    num = int(input())

    while cnt < num:
      cnt += 1
      stack.append(cnt)
      result.append("+")

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        tmp = False

if tmp == False:
    print("NO")
else:
    print("\n".join(result))