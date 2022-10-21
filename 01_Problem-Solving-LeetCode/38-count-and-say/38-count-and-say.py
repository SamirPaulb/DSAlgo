class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for i in range(n-1):
            n = len(res)
            j = 0
            tmp = ''
            while j < n:
                count = 1
                ch = res[j]
                k = j+1
                while k < n and res[k] == res[k-1]:
                    count += 1
                    k += 1
                j = k
                tmp += str(count) + res[j-1]
            res = tmp
        
        return res