# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        cnt = collections.Counter(nums)
        numset = sorted(list(cnt.keys()))
        i = 0
        while i < len(numset):
            c = numset[i]
            if cnt[c] > 0:
                for j in range(k):
                    cnt[c+j] -= 1
                    if cnt[c+j] < 0: return False
            else:
                i += 1
        
        return True
      

# Time: O(N log(N))
