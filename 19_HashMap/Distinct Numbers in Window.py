# https://www.interviewbit.com/problems/distinct-numbers-in-window/

class Solution:
	def dNums(self, A, B):
		dic = {}
		count = 0
		res = []

		for i in range(len(A)):
			if i < B:
				if A[i] not in dic:
					dic[A[i]] = 1
					count += 1
				else:
					dic[A[i]] += 1
			else:
				dic[A[i-B]] -= 1
				if dic[A[i-B]] == 0: count -= 1
				if A[i] not in dic:
					dic[A[i]] = 1
					count += 1
				else:
					if dic[A[i]] == 0:
						dic[A[i]] += 1
						count += 1
					else:
						dic[A[i]] += 1
			
			if i >= B-1: res.append(count)
		
		return res


# Time: O(N)
# Space: O(N)
