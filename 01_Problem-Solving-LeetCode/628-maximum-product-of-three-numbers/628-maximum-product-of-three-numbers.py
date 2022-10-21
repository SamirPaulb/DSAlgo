class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        mini = [2**31] * 2
        maxi = [-2**31] * 3
        
        for num in nums:
            if num < mini[1]:
                mini[1] = num
                mini.sort()
            if num > maxi[0]:
                maxi[0] = num
                maxi.sort()
        
        min1, min2 = mini
        max1, max2, max3 = maxi
        return max(min1*min2*max3, max1*max2*max3)