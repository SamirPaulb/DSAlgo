# https://practice.geeksforgeeks.org/problems/subset-sums2234/1#

'''
Make the recursion TREE of the problem. one chile including the current element
and other child Not including the current element
'''
class Solution:
	def subsetSums(self, arr, N):
		res = []
		def solve(i, s):
		    if i == len(arr):
		        res.append(s)
		        return
            # make 2 calls for 2 childs of the recursion tree
            solve(i+1, s + arr[i])  # Include the current element 
            solve(i+1, s)           # NOT include the current element
        
        solve(0, 0)
        return res
		
# Time: O(2 ^ N)  # as for each element we are calling 2 different calls
# Space: O(N)