# https://www.geeksforgeeks.org/find-the-size-of-largest-subset-with-positive-bitwise-and/

# Python 3 program for the above approach

# Function to find the largest possible
# subset having Bitwise AND positive
def largestSubset(a, N):
	# Stores the number of set bits
	# at each bit position
	bit = [0 for i in range(32)]

	# Traverse the given array arr[]
	for i in range(N):
		# Current bit position
		x = 31

		# Loop till array element
		# becomes zero
		while(a[i] > 0):
			# If the last bit is set
			if (a[i] & 1 == 1):

				# Increment frequency
				bit[x] += 1

			# Divide array element by 2
			a[i] = a[i] >> 1

			# Decrease the bit position
			x -= 1

	# Size of the largest possible subset
	print(max(bit))

# Driver Code
if __name__ == '__main__':
	arr = [7, 13, 8, 2, 3]
	N = len(arr)
	largestSubset(arr, N)

	# This code is contributed by ipg016107.

