def check(num):
    result = 0

N = int(input())
for i in range(1, N+1):
    current = str(i)
    clap = current.count('3') + current.count('6') + current.count('9')

    if clap == 0:
        print(current, end = ' ')
    else:
        print('-' * clap, end = ' ')