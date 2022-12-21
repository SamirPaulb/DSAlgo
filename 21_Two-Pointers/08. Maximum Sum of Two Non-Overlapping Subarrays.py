# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        prefixArr = []
        s = 0
        for i in nums:
            s += i
            prefixArr.append(s)
        
        def left(k):
            arr = [0] * n
            curmax = 0
            for i in range(k-1, n):
                cur = prefixArr[i] - prefixArr[i-k+1] + nums[i-k+1]
                curmax = max(curmax, cur)
                arr[i] = curmax
            return arr
        
        def right(k):
            arr = [0] * n
            curmax = 0
            for i in range(n-k, -1, -1):
                cur = prefixArr[i+k-1] - prefixArr[i] + nums[i]
                curmax = max(curmax, cur)
                arr[i] = curmax
            return arr
        
        first_left = left(firstLen)
        first_right = right(firstLen)
        second_left = left(secondLen)
        second_right = right(secondLen)
        
        res = 0
        for i in range(1, n):
            a = first_left[i-1] + second_right[i]
            b = second_left[i-1] + first_right[i]
            res = max(res, a, b)
        
        return res
