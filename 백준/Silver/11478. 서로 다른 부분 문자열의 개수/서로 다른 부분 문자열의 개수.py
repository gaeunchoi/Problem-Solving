S = input()

str_list = set()
for i in range(len(S)):
    for j in range(i, len(S)):
        str_list.add(S[i:j+1])

print(len(str_list))