# https://www.interviewbit.com/problems/sum-of-pairwise-hamming-distance/ 

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def hammingDistance(self, A):
		res = 0
		for i in range(32):
			n0 = n1 = 0
			for a in A:
				if a & (1<<i):
					n1 += 1
				else:
					n0 += 1
			res += 2 * n0 * n1
			
		return res % 1000000007
