str = input().upper()
list = list(set(str))
cnt = [str.count(i) for i in list]

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(list[cnt.index(max(cnt))])

