class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ngeDict = {}
        stack = []
        for i in nums2:
            while stack and stack[-1] < i:
                a = stack.pop()
                ngeDict[a] = i
            stack.append(i)

        res = []
        for i in nums1:
            if i in ngeDict:
                res.append(ngeDict[i])
            else:
                res.append(-1)
        
        return res