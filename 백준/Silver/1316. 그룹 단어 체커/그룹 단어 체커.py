n = int(input())
num = n

for i in range(n):
    str = input()

    for j in range(len(str)-1):
        if str[j] == str[j+1]:
            pass
        elif str[j] in str[j+1:]:
            num -= 1
            break

print(num)