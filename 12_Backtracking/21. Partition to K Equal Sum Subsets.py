# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
'''
1. if sums[j] == 0: break

The key is, sums[j] == 0 means for all k > j, sum[k] == 0; because this algorithm always fill the previous buckets before trying the next.
So if by putting nums[i] in this empty bucket can't solve the game, putting nums[i] on other empty buckets can't solve the game either.

2. nums.sort(reverse=True)

Always start from big numbers for this kind of problem, just by doing it yourself for a few times you will find out that the big numbers are the easiest to place.
'''

class Solution:
    def canPartitionKSubsets(self, nums, k):
        nums.sort(reverse=True)
        subsets, target = [0] * k, sum(nums)//k
        
        def backtrack(idx):
            if idx == len(nums):
                return True
            for i in range(k):
                subsets[i] += nums[idx]
                if subsets[i] <= target and backtrack(idx+1): 
                    return True
                subsets[i] -= nums[idx]
                if subsets[i] == 0: 
                    break
            return False
        
        return backtrack(0)
    
# Time: O(n * 2^k)
# Space: O(n * 2^k)


'''
# https://youtu.be/h_6MldQ8vB8?t=121

class Solution:
    def canPartitionKSubsets(self, nums, k):
        if sum(nums) % k: 
            return False
        nums.sort(reverse = True)
        target = sum(nums)//k
        used = [False] * len(nums)
        
        def backtrack(i, k, subsetSum):
            if k == 0: 
                return True
            if subsetSum == target:
                return backtrack(0, k-1, 0)
            if i >= len(nums) or subsetSum > target:
                return False
            if used[i]:
                return backtrack(i+1, k, subsetSum)
            # Pick the urrent element
            used[i] = True
            pick = backtrack(i+1, k, subsetSum + nums[i])
            used[i] = False
            # Skip the current element
            skip = backtrack(i+1, k, subsetSum)
            return pick or skip
        
        return backtrack(0, k, 0)
    
    
# Time: O(k * 2^n)
# Space: O(k * 2^n)
'''
