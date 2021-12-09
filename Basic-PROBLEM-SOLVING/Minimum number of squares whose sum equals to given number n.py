# https://www.geeksforgeeks.org/minimum-number-of-squares-whose-sum-equals-to-given-number-n/
# Minimum number of squares whose sum equals to given number n
# A naive recursive Python program to
# find minimum number of squares whose
# sum is equal to a given number

# Returns count of minimum squares
# that sum to n
def getMinSquares(n):

	# base cases
	if n <= 3:
		return n

	# getMinSquares rest of the table
	# using recursive formula
	# Maximum squares required
	# is n (1 * 1 + 1 * 1 + ..)
	res = n

	# Go through all smaller numbers
	# to recursively find minimum
	for x in range(1, n + 1):
		temp = x * x
		if temp > n:
			break
		else:
			res = min(res, 1 + getMinSquares(n - temp))
	
	return res

# Driver code
print(getMinSquares(6))


'''
Output = 3
'''