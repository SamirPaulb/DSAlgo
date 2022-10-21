import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        copyNums = self.nums.copy()
        n = len(self.nums)
        for i in range(n):
            j = random.randint(i, n-1)
            copyNums[i], copyNums[j] = copyNums[j], copyNums[i]
        return copyNums
    
            
    
    
    
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()