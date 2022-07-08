# https://www.geeksforgeeks.org/postfix-to-infix/
# Postfix to Infix

exp = input("")
stack = []

for i in exp:
	if i not in "+-*/^":
		stack.append(i)
	else:
		a = stack.pop()
		b = stack.pop()
		stack.append("(" + b + i + a + ")")

print("".join(stack))
