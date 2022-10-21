class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mp = {}
        for i in arr:
            if i not in mp:
                mp[i] = 1
            else:
                mp[i] += 1
        
        occurrences = list(mp.values())
        return len(set(occurrences )) == len(occurrences )