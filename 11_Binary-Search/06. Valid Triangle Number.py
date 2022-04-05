# https://leetcode.com/problems/valid-triangle-number/
# https://youtu.be/PqEiJDdt3S4

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        
        for i in range(len(nums)-1, 1, -1):
            r = i - 1
            l = 0
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    res += (r - l)
                    r -= 1
                else:
                    l += 1
        
        return res

# Time: O(N^2)
# Space: O(1)
