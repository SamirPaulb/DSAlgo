class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()                  # for smallest lexicographical order
        visited = {""}                # hashset to keep a track of visited words
        res = ''
        
        for word in words:
            if word[:-1] in visited:     # check previous word ie. word[:len(word)-1] visited or not
                visited.add(word)        # add this word to the set
                if len(word) > len(res): # current word have greater lenght and lexicographically smaller
                    res = word           # update res
        
        return res
    
    
    
# Time: O(n log(n))   # for sorting the words
# Space: O(n)         # for making the set visited