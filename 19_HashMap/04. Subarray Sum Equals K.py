# https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        curSum = 0
        res = 0
        
        for num in nums:
            curSum += num
            if (curSum - k) in hashmap:
                res += hashmap[curSum - k]
            if curSum not in hashmap:
                hashmap[curSum] = 1
            else:
                hashmap[curSum] += 1
        
        return res

        