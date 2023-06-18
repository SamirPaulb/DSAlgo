# https://leetcode.com/problems/special-permutations/

'''
The Logic is to iterate over the array of numbers. For each iteration, We choose an element based on the condition 
(prev % nums[j] == 0 || nums[j] % prev == 0), where prev represents the previously chosen element.

If the condition is satisfied, it means the current number can be chosen. To keep track of the chosen numbers, 
a bitmask (mask) is used. Each bit in the bitmask represents a number that has been chosen. By setting the corresponding 
bit in the bitmask for the current index, we indicate that the number at that index has been chosen.

After updating the bitmask, the code recursively calls itself, moving to the next index and incrementing the count. 
The recursion continues until all numbers have been chosen.

If, at the end of the recursion, all numbers have been chosen (i.e., all bits in the bitmask are set), 
the count is incremented by 1. This means a valid permutation has been found.

In summary, the code uses bitmasking to represent chosen numbers and recursively explores all possible permutations, 
incrementing the count whenever a valid permutation is found.
'''

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(indx, prev, mask):
            if mask >= (1<<n)-1: return 1
            ans = 0
            for i in range(n):
                if not (mask & (1<<i)) and (prev % nums[i] == 0 or nums[i] % prev == 0):
                    ans += dfs(indx+1, nums[i], mask | (1<<i))
            return ans % (10**9 + 7)
        
        return dfs(0, -1, 0)

# Time complexity: O(2 ^ n * n * n * n)
# Space complexity: O(2 ^ n * n * n)




'''
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n, MOD = len(nums), 10**9 + 7
        used = set()
        def dfs(index=0, prev=1):
            if index == n: return 1
            count = 0
            for i in range(n):
                if not (nums[i] in used) and (nums[i] % prev == 0 or prev % nums[i] == 0):
                    used.add(nums[i])
                    count += dfs(index + 1, nums[i])
                    used.remove(nums[i])
            return count % MOD
        return dfs()
# while it seems to be correct, it TLE's on test case 529/587. So the bitmask is used so that the dfs function could be cached and run faster.
'''
