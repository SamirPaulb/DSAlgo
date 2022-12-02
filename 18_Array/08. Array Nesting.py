# https://leetcode.com/problems/array-nesting/description/


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 1
        visited_indeces = set()

        for i in range(len(nums)):
            visited_num = set()
            tmp = 0
            cur = nums[i]
            while cur not in visited_num:
                tmp += 1
                visited_num.add(cur)
                if cur in visited_indeces: break
                visited_indeces.add(cur)
                cur = nums[cur]
            res = max(res, tmp)
        
        return res


# Time: O(N)
# Space: O(N*N)
