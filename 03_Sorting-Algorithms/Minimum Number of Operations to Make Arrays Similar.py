# # https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/

'''Intuition:
# Only odd numbers can be chaged to odd numbers and even to even hence separate them.
# Now minimum steps to make 'nums' to 'target' is by converting max of 'nums' to max of 'target'.
# Every number in 'nums' can be paired with a number in 'target' by index hence sorting.
# Now we need only the number of positives or number of negatives.
'''

class Solution:
    def makeSimilar(self, nums, target):
        nums_odd = sorted([i for i in nums if i%2 == 1])
        nums_even = sorted([i for i in nums if i%2 == 0])
        
        target_odd = sorted([i for i in target if i%2 == 1])
        target_even = sorted([i for i in target if i%2 == 0])
        
        res = 0
        for n, t in zip(nums_odd, target_odd):
            if n > t: res += n - t
        for n, t in zip(nums_even, target_even):
            if n > t: res += n - t
        
        return res//2
    
    
    
# Time: O(N log(N))
# Space: O(N)
