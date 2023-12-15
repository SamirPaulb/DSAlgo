# https://leetcode.com/problems/repeated-dna-sequences/description/

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        dic = {'A':0, 'C':1, 'G': 2, 'T':3}
        n = len(s)
        if n < 10: return []
        initial_val = 0
        st = set()
        ans = set()
        for i in range(n - 9):

            if i == 0: 
                for j in range(i, i + 10):
                    initial_val <<= 2
                    initial_val |=dic[s[j]]
            else:
                initial_val &= ((1 << 18)- 1)
                initial_val <<= 2
                initial_val |= dic[s[i+9]]            
            
            if initial_val in st:
                ans.add(s[i:i+10])
                continue
            st.add(initial_val)
        
        return ans   