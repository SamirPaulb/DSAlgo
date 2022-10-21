class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        stack = []
        for i, ch in enumerate(nums):
            rem = n - (i+1)
            while stack and stack[-1] > ch and rem >= k - len(stack):
                stack.pop()
            stack.append(ch)
        
        return stack[:k]
        