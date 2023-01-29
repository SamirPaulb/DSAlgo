# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        prefixSum = []
        total = 0
        
        for point in cardPoints:
            prefixSum.append(total)
            total += point
        prefixSum.append(total)
        
        miniSubarraySum = 2**31
        for i in range(n-k, len(cardPoints)+1):
            miniSubarraySum = min(miniSubarraySum, prefixSum[i] - prefixSum[i-(n-k)])
        
        return sum(cardPoints) - miniSubarraySum
      
      
