class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def dfs(s, path, dots):
            if dots > 4: return 
            if dots == 4 and not s:
                res.append(path[:-1])
                return

            for i in range(1, len(s)+1):
                if s[:i] == '0' or (s[0] != '0' and 0 < int(s[:i]) < 256):
                    dfs(s[i:], path + s[:i] + '.', dots+1)


        dfs(s, "", 0)
        return res