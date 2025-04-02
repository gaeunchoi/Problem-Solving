message = input()
for i in range(len(message)):
    print(ord(message[i]) - 64, end = ' ')