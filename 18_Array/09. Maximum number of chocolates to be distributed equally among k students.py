# https://www.geeksforgeeks.org/maximum-number-chocolates-distributed-equally-among-k-students/

'''
Given n boxes containing some chocolates arranged in a row. There are k number of students. 
The problem is to distribute maximum number of chocolates equally among k students by selecting
a consecutive sequence of boxes from the given lot. Consider the boxes are arranged in a row with
numbers from 1 to n from left to right. We have to select a group of boxes which are in consecutive
order that could provide maximum number of chocolates equally to all the k students. An array arr[]
is given representing the row arrangement of the boxes and arr[i] represents number of chocolates
in that box at position ‘i’.

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
	
	prev_rem, cur_rem, maxSum = {}, 0, 0
	
	# 'prefixSum[]' to store cumulative prefix sum,
	# where prefixSum[i] = prefixSum(arr[0]+..arr[i])
	prefixSum = [0]*n
	prefixSum[0] = arr[0]
	
	# building up 'prefixSum[]'
	for i in range(1, n):
		prefixSum[i] = prefixSum[i - 1] + arr[i]
		
	# traversing 'prefixSum[]'
	for i in range(n):

		# finding current remainder
		cur_rem = prefixSum[i] % k
		
		if (cur_rem == 0 and maxSum < prefixSum[i]) :
			maxSum = prefixSum[i]
		elif (cur_rem not in prev_rem) :
			prev_rem[cur_rem] = i
		elif (maxSum < (prefixSum[i] - prefixSum[prev_rem[cur_rem]])):
			maxSum = prefixSum[i] - prefixSum[prev_rem[cur_rem]]
																						
	return maxSum//k
	
# Driver program to test above
arr = [ 2, 7, 6, 1, 4, 5 ]
n, k = len(arr), 3

print("Maximum number of chocolates: " +
	str(maxNumOfChocolates(arr, n, k)))

