# https://www.lintcode.com/problem/3684/

class Solution:
    def smallest_common_element(self, mat: List[List[int]]) -> int:
        cnt = {}
        for i in range(len(mat)):
            rowset = set()
            for j in range(len(mat[0])):
                if mat[i][j] not in rowset:
                    if mat[i][j] not in cnt: cnt[mat[i][j]] = 1
                    else: cnt[mat[i][j]] += 1
                    rowset.add(mat[i][j])
        
        res = 2**31
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if cnt[mat[i][j]] == len(mat) and mat[i][j] < res:
                    res = mat[i][j]
        
        return res if res != 2**31 else -1

# Time: O(N^2)
