# https://leetcode.com/problems/matchsticks-to-square/


class Solution:
    def makesquare(self, nums):
        # If number of matchsticks less than 4, then we can't form any square
        if len(nums) < 4:
            return False

        # Perimeter of our square (if one can be formed)
        perimeter = sum(nums)

        # Possible side of our square.
        possible_side =  perimeter // 4

        # If the perimeter can be equally split into 4 parts (and hence 4 sides, then we move on).
        if possible_side * 4 != perimeter:
            return False

        # Reverse sort the matchsticks because we want to consider the biggest one first.
        nums.sort(reverse=True)

        # This array represents the 4 sides and their current lengths
        sides = [0] * 4

        # Our recursive dfs function.
        def dfs(index):

            # If we reach the end of matchsticks array, we check if the square was formed or not
            if index == len(nums):
                # If sides are equal
                return sides[0] == sides[1] == sides[2] == sides[3] == possible_side

            # The current matchstick can belong to any of the 4 sides (provided their remaining lenghts are >= the size of the current matchstick)
            for i in range(4):
                # If this matchstick can fir in the space left for the current side
                if sides[i] + nums[index] <= possible_side:
                    # Recurse
                    sides[i] += nums[index]
                    if dfs(index + 1):
                        return True
                    # Revert the effects of recursion because we no longer need them for other recursions.
                    sides[i] -= nums[index]
            return False  
        
        return dfs(0)
