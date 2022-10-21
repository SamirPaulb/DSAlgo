class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n =  len(s)
        countDict = {}
        for i in range(n-10+1):
            seq = s[i:i+10]
            if seq not in countDict: countDict[seq] = 1
            else: countDict[seq] += 1
        
        res = [seq for seq in countDict if countDict[seq] >= 2]
        
        return res