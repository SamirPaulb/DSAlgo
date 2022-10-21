class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        
        dp = [0] * len(rating)
        for i in range(len(rating)):
            for j in range(i, -1, -1):
                if rating[i] > rating[j]:
                    dp[i] += 1
                    count += dp[j]
        
        dp = [0] * len(rating)
        for i in range(len(rating)):
            for j in range(i, -1, -1):
                if rating[i] < rating[j]:
                    dp[i] += 1
                    count += dp[j]
        
        return count