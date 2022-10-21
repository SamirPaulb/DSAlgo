class Solution:
    def longestPalindrome(self, s: str) -> int:
        countDict = {}
        for i in s:
            if i not in countDict:
                countDict[i] = 1
            else:
                countDict[i] += 1
        
        res = 0
        firstOdd = False
        for i in countDict:
            if countDict[i] % 2 == 0:
                res += countDict[i]
            else:
                if not firstOdd: 
                    res += 1
                    firstOdd = True
                res += countDict[i] - 1
        print(countDict)
        return res