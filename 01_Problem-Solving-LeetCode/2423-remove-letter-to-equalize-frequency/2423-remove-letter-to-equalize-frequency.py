# https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = collections.Counter(word)
        for c in word:
            counter[c] -= 1
            if counter[c] == 0:
                counter.pop(c)
            if len(set(counter.values())) == 1: return True
            counter[c] += 1
        
        return False
    


class Solution:
    def equalFrequency(self, word: str) -> bool:
        dct = {}
        for i in word:
            if i in dct: dct[i] += 1
            else: dct[i] = 1
        
        for i in word:
            dct[i] -= 1
            if dct[i] == 0:
                del dct[i]
                if len(set(dct.values())) == 1: return True
                dct[i] = 1
            else:
                if len(set(dct.values())) == 1: return True
                dct[i] += 1
        
        return False