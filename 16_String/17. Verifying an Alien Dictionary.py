# https://leetcode.com/problems/verifying-an-alien-dictionary/

''' 
If a sequence of words is sorted, then each adjacent word of the sequence must also be sorted.

👉 Lexicographically Sorted when -
    ✦ If at first mismatch, mp[a[i]] < mp[b[i]], or
    ✦ If each letters of both words match and length(a) <= length(b)

👉 Not Lexicographically Sorted when -
    ✦ If at first mismatch, mp[a[i]] > mp[b[i]], or
    ✦ If each letters of both words match and length(a) > length(b).

'''

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ind = {c:i for i,c in enumerate(order)}
        def checkOrder(w1, w2):
            for s1, s2 in zip(w1, w2):
                if ind[s1] != ind[s2]:
                    return ind[s1] < ind[s2]
            return len(w1) <= len(w2)
        
        return all(checkOrder(w1, w2) for w1, w2 in zip(words, words[1:]))

                
        
'''
✦ Time Complexity : O(N),   where N is the total number of characters in words.

✦ Space Complexity : O(1),  we only need constant amount of space to store the mapping of letters to index which does not depend on the size of input. Hence we get constant space complexity.
'''
