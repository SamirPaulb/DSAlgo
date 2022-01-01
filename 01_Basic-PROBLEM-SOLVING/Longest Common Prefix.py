class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        if len(strs) ==1:
            return strs[0]
        
        start = strs[0]
        result  = ""
        for i in range(0,len(strs)):
            temp = strs[i]
            if start != temp:
                a = min(start,temp)
                b = max(start, temp)
                for j in range(len(a)):
                    if a[j] == b[j]:
                        result += a[j] 
                    else:
                        break
                start = result
                result = ""
        return start


strs = ["ab","a"]
ll = Solution()
print(ll.longestCommonPrefix(strs))


      
