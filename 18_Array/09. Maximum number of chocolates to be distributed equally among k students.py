'''
Given n boxes containing some chocolates arranged in a row. There are k number of students. The problem is to distribute maximum number of chocolates equally among k students by selecting a consecutive sequence of boxes from the given lot. Consider the boxes are arranged in a row with numbers from 1 to n from left to right. We have to select a group of boxes which are in consecutive order that could provide maximum number of chocolates equally to all the k students. An array arr[] is given representing the row arrangement of the boxes and arr[i] represents number of chocolates in that box at position ‘i’.

The problem is to find maximum sum sub-array divisible by k and then return (sum / k).


Examples: 

Input : arr[] = {2, 7, 6, 1, 4, 5}, k = 3
Output : 6
The subarray is {7, 6, 1, 4} with sum 18.
Equal distribution of 18 chocolates among
3 students is 6.
Note that the selected boxes are in consecutive order
with indexes {1, 2, 3, 4}.

'''


# Python3 implementation to
# find the maximum number
# of chocolates to be
# distributed equally
# among k students

# function to find the
# maximum number of chocolates
# to be distributed equally
# among k students
def maxNumOfChocolates(arr, n, k):
	
	um, curr_rem, maxSum = {}, 0, 0
	
	# 'sm[]' to store cumulative sm,
	# where sm[i] = sm(arr[0]+..arr[i])
	sm = [0]*n
	sm[0] = arr[0]
	
	# building up 'sm[]'
	for i in range(1, n):
		sm[i] = sm[i - 1] + arr[i]
		
	# traversing 'sm[]'
	for i in range(n):

		# finding current remainder
		curr_rem = sm[i] % k
		
		if (not curr_rem and maxSum < sm[i]) :
			maxSum = sm[i]
		elif (not curr_rem in um) :
			um[curr_rem] = i
		elif (maxSum < (sm[i] - sm[um[curr_rem]])):
			maxSum = sm[i] - sm[um[curr_rem]]
		
	return maxSum//k
	
# Driver program to test above
arr = [ 2, 7, 6, 1, 4, 5 ]
n, k = len(arr), 3

print("Maximum number of chocolates: " +
	str(maxNumOfChocolates(arr, n, k)))

