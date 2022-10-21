class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = None
        prevDiff = float("inf")
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: continue # if two consecutive elelments are same then for the first same nums[i] < l < r one res if added. so no need to add same repeted res.
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if abs(target - threeSum) < prevDiff: 
                    ans = threeSum
                    prevDiff = abs(target - threeSum)
                if threeSum < target: l += 1
                elif threeSum > target: r -= 1
                else: return threeSum
        
        return ans
                