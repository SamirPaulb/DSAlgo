# https://leetcode.com/problems/maximum-product-of-word-lengths/

'''
class Solution:
    def maxProduct(self, words):
        wordDict = {}
        for word in words:
            wordDict[word] = [False]*26
            for w in word:
                wordDict[word][ord(w) - ord('a')] = True
        
        res = 0
        for i, w1 in enumerate(words):
            for w2 in words[i+1:]:
                flag = True
                for j in range(26):
                    if wordDict[w1][j] and wordDict[w2][j]:
                        flag = False
                if flag:
                    res = max(res, len(w1) * len(w2))
        
        return res   
'''


# Solving the above using bitmanipulation.
# instead of using a bool array in dictionary use a binary number of 26bits
# where 1 represent that letter is present and 0 means not.
# if we & of 2 word != 0 means any common bit. 
    
class Solution:
    def maxProduct(self, words):
        wordDict = {}
        for word in words:
            wordDict[word] = 0
            for w in word:
                wordDict[word] |= 1 << (ord(w) - ord('a'))
        
        res = 0
        for i, w1 in enumerate(words):
            for w2 in words[i+1:]:
                if not wordDict[w1] & wordDict[w2]: # 0
                    res = max(res, len(w1) * len(w2))
        
        return res  
        
# Time Complexity : O(n*(N+n))
