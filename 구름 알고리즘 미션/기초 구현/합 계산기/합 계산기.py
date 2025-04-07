T = int(input())

result = 0
for _ in range(T):
	num1, oper, num2 = map(str, input().split(" "))
	if oper == '+':
		result += int(num1) + int(num2)
	elif oper == '-':
		result += int(num1) - int(num2)
	elif oper == '*':
		result += int(num1) * int(num2)
	else:
		result += int(num1) // int(num2)

print(result)