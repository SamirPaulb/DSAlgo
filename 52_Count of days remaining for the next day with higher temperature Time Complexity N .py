# Function to determine how many days required to wait for the next warmer day
def dailyTemperatures(T):

	n = len(T)

	# To store the answer
	daysOfWait = [-1] * n
	s = []

	# Traverse all the temperatures
	for i in range(n):

		# Check if current index is the
		# next warmer temperature of
		# any previous indexes
		while(len(s) != 0 and
			T[s[-1]] < T[i]):
			daysOfWait[s[-1]] = i - s[-1]

			# Pop the element
			s.pop(-1)

		# Push the current index
		s.append(i)

	# Print waiting days
	for i in range(n):
		print(daysOfWait[i], end = " ")

# Driver Code

# Given temperatures
arr = [ 73, 74, 75, 71, 69, 72, 76, 73 ]

# Function call
dailyTemperatures(arr)

# This code is contributed by Shivam Singh
