T = int(input())

base64_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')
for tc in range(1, T+1):
    word = list(input())
    value = ''

    for i in range(len(word)):
        num = base64_list.index(word[i])
        binary_num = str(bin(num)[2:])

        while len(binary_num) < 6:
            binary_num = '0' + binary_num
        value += binary_num

    result = ''
    for i in range(len(word)*6 // 8):
        num = int(value[i*8 : i*8 + 8], 2)
        result += chr(num)
    print(f'#{tc} {result}')