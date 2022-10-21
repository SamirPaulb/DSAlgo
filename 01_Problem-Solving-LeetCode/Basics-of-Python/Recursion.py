def factorial(n):
	if i == 0 or i == 1 : #Base condition which doesn’t call the function any further
		return i
	else:
		return n*factorial(n-1) #Function calling itself
