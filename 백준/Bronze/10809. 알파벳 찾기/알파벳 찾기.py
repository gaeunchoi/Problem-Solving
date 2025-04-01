str = input()

# 아스키 코드로 a=97, z=122이므로 대응하는 숫자 list로
alpha = list(range(97, 123))

for i in alpha:
    # chr(숫자) -> 숫자에 맞는 아스키코드 반환
    # find 함수 -> 문자열 안에서 찾는 문자가 첫 번째에 위치한 순서 숫자로 출력
    print(str.find(chr(i)), end=" ")