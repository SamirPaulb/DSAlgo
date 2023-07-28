# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

class Solution:
    def countKDifference(self, nums, k):
        cnt = collections.Counter()
        for n in nums:
            cnt[n] += 1
            
        res = 0
        taken = set()
        for n in cnt:
            l, r = n-k, n+k
            if l not in taken: 
                res += cnt[n] * cnt[l]
            if r not in taken:
                res += cnt[n] * cnt[r]
            taken.add(n)
        
        return res
        
    
'''    
class Solution:
    def countKDifference(self, nums, k):
        seen = {num:0 for num in nums}
        count = 0
        
        for num in nums:
            tmp1 = num - k;  tmp2 = num + k
            if tmp1 in seen:
                count += seen[tmp1]
            elif tmp2 in seen:
                count += seen[tmp2]
            seen[num] += 1
        
        return count
'''


# Time: O(N)
# Space: O(N)
