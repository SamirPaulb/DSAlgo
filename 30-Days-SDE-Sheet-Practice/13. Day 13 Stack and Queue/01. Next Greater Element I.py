# https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextGreaterDic = {ch:-1 for ch in nums2}
        
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                nextGreaterDic[nums2[stack.pop()]] = nums2[i]
            stack.append(i)
        
        for i, ch in enumerate(nums1):
            nums1[i] = nextGreaterDic[ch]
        
        return nums1
        