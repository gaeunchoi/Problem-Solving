input_word = input()
if ''.join(reversed(input_word)) == input_word:
    print(1)
else:
    print(0)