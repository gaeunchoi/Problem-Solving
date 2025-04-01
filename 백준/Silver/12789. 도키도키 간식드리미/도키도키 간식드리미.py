N = int(input())

s = []
target = 1
students = list(map(int, input().split()))

while students:
    if students[0] == target:
        students.pop(0)
        target += 1
    else:
        s.append(students.pop(0))

    while s:
        if s[-1] == target:
            s.pop()
            target += 1
        else:
            break

print('Nice' if not s else 'Sad')