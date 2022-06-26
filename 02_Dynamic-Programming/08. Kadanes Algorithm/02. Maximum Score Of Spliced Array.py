# https://leetcode.com/problems/maximum-score-of-spliced-array/

class Solution:
    def maximumsSplicedArray(self, A, B):
        def kadane(A, B):
            # calculate how much B can earn by swaping a part of the array.
            res = cur = 0
            for i in range(len(A)):
                # Once the element in A make the cur negative, reset cur to zero; else, update cur.
                cur = max(0, cur + A[i] - B[i])
                res = max(res, cur)
            # return the sum after swapping a part of the array.
            return res + sum(B)
        
        # We are not sure which array is bigger so that we have to do kadane() twice.
        return max(kadane(A, B), kadane(B, A))
    
'''
Time: O(n)
Space: O(1)
'''
