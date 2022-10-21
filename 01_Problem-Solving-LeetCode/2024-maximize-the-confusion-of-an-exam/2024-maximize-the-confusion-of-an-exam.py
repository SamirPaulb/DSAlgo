class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l = 0; r = 0
        frequency = {}
        maxFrequency = 0
        ans = 0
        
        for r in range(len(answerKey)):
            if answerKey[r] not in frequency:
                frequency[answerKey[r]] = 1
            else:
                frequency[answerKey[r]] += 1
            maxFrequency = max(maxFrequency, frequency[answerKey[r]])
            
            while r - l - maxFrequency >= k:
                frequency[answerKey[l]] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)
        
        return ans