# https://practice.geeksforgeeks.org/problems/find-nth-root-of-m5843/1/

# https://youtu.be/WjpswYrS2nY

class Solution:
	def NthRoot(self, n, num):
		r = num
		l = 1
		
		while  l <= r:
		    mid = (l + r) // 2
		    if mid ** n < num:
		        l = mid + 1
		    elif mid ** n > num:
		        r = mid - 1
		    else:
		        return mid
		        
		return -1

# Time: O(log(num))
# Space: O(1)